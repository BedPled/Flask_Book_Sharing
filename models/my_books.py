import pandas as pandas

def get_book_by_param(conn, city, genre, lang, author_name, book_title):
    return pandas.read_sql('''
        SELECT  title, genre_name, author_name, language_name, price, description,
                country_name || ', г.' || city_name || ', ул.' || street as location,
                u.id_user, ba.id_book
        FROM book
            join genre g on g.id_genre = book.id_genre
            join book_author ba on ba.id_book = book.id_book_author and book.id_book_author = ba.id_book
            join author a on a.id_author = ba.id_author
            join language l on l.id_language = book.id_language
            join give_or_take got on book.id_book = got.id_book
            join user u on got.id_user = u.id_user
            join address a2 on a2.id_address = u.id_address
            join city c on c.id_city = a2.id_city
            join country c2 on c2.id_country = c.id_country
        WHERE   id_gt_status = 2 AND is_su_status = 1 
            AND city_name LIKE '%{city}' 
            AND genre_name LIKE '%{genre}'
            AND language_name LIKE '%{lang}'
            AND author_name LIKE '%{author_name}%'
            AND book.title LIKE '%{book_title}%'
    '''.format(city=city,
               genre=genre,
               lang=lang,
               author_name=author_name,
               book_title=book_title),
                           conn)


# вывод книг пользователя с определённым статусов (Моя / Отдаю)
def get_user_book(conn, user):
    """
    Функция вывода книг пользователя с определённым статусов (Моя / Отдаю)
    1 - моя
    2 - отдаю
    """
    return pandas.read_sql('''
        SELECT title, genre_name, author_name, language_name, price, description, id_gt_status, ba.id_book 
        FROM book
            join genre g on g.id_genre = book.id_genre
            join book_author ba on ba.id_book = book.id_book_author and book.id_book_author = ba.id_book
            join author a on a.id_author = ba.id_author
            join language l on l.id_language = book.id_language
            join give_or_take got on book.id_book = got.id_book
        WHERE id_user == :id AND is_su_status = 1; -- моя книга
    ''', conn, params={"id": user})

def get_my_requests(conn, USER_ID):
    return pandas.read_sql('''
    SELECT title, genre_name, author_name, language_name, price, description,
           country_name || ', г.' || city_name || ', ул.' || street as location,
           us_status_name, ba.id_book
    FROM book
        join genre g on g.id_genre = book.id_genre
        join book_author ba on ba.id_book = book.id_book_author and book.id_book_author = ba.id_book
        join author a on a.id_author = ba.id_author
        join language l on l.id_language = book.id_language
        join give_or_take got on book.id_book = got.id_book
        join us_status us on us.id_us_status = got.is_su_status
        join user u on got.id_user = u.id_user
        join address a2 on a2.id_address = u.id_address
        join city c on c.id_city = a2.id_city
        join country c2 on c2.id_country = c.id_country
    WHERE u.id_user == :id
        AND is_su_status != 1
        AND is_su_status != 4
        AND id_gt_status = 2;
    ''', conn,  params={"id": USER_ID})

def get_my_gives(conn, USER_ID):
    return pandas.read_sql('''
    SELECT title, genre_name, author_name, language_name, price, description,
           u.login , u.messanger , got.id_book, got.id_user
    FROM book
        join genre g on g.id_genre = book.id_genre
        join book_author ba on ba.id_book = book.id_book_author and book.id_book_author = ba.id_book
        join author a on a.id_author = ba.id_author
        join language l on l.id_language = book.id_language
        join give_or_take got on book.id_book = got.id_book
        join us_status us on us.id_us_status = got.is_su_status
        join user u on got.id_user = u.id_user
        join address a2 on a2.id_address = u.id_address
        join city c on c.id_city = a2.id_city
        join country c2 on c2.id_country = c.id_country
    WHERE book.id_book IN (     SELECT book.id_book
                                FROM book
                                join give_or_take t on book.id_book = t.id_book
                                join user u2 on u2.id_user = t.id_user
                                WHERE t.id_user = :id
                                AND is_su_status = 1)
        AND u.id_user != :id
        AND is_su_status = 2
        AND id_gt_status = 2
    ORDER BY title;
    ''', conn,  params={"id": USER_ID})


def set_book_gt_status(conn, id_user, id_book, id_status):
    """
    Функция для смены GT статуса книги.
    1 - моя
    2 - отдаю
    """
    cur = conn.cursor()
    cur.executescript(f'''
    UPDATE give_or_take SET id_gt_status = {id_status}
    WHERE   id_book = {id_book} 
        AND id_user = {id_user}
    ''')
    return conn.commit()


def set_book_us_status(conn, id_user, id_book, id_status):
    """
    Функция для смены US статуса книги.
    1 - без статуса
    2 - рассмотрение
    3 - отклонена
    4 - удалена
    """
    cur = conn.cursor()
    print(f'''
    UPDATE give_or_take SET is_su_status = {id_status}
    WHERE id_book = {id_book} AND id_user = {id_user}
    ''')

    cur.executescript(f'''
    UPDATE give_or_take SET is_su_status = {id_status}
    WHERE id_book = {id_book} AND id_user = {id_user}
    ''')
    return conn.commit()

def check_request(conn, id_book, USER_ID):
    return pandas.read_sql('''
        SELECT id_book, id_user, id_gt_status, is_su_status
        FROM give_or_take
        WHERE   id_book = :id_book
            AND id_user = :USER_ID
            AND id_gt_status = 2
            AND is_su_status = 2
    ''', conn, params={
        "id_book": id_book,
        "USER_ID": USER_ID
    })

def request_button(conn, id_book, USER_ID):
    cur = conn.cursor()

    cur.executescript('''
    INSERT INTO give_or_take (id_book, id_user, id_gt_status, is_su_status)
    VALUES ({id_book}, {USER_ID}, 2, 2)
    '''.format(id_book=id_book,
               USER_ID=USER_ID))

    return conn.commit()


def accept_and_cancel_rest_requests(conn, id_book, id_user):
    """
    Функция отменяет все заявки кроме заявки {id_user} пользователя
    1 - без статуса
    2 - рассмотрение
    3 - отклонена
    4 - удалена
    """
    cur = conn.cursor()
    cur.executescript(f'''
    UPDATE give_or_take SET is_su_status = 3
    WHERE   id_book = {id_book} 
        AND id_user != {id_user}
        AND id_gt_status = 2
        AND is_su_status = 2;
    
    UPDATE give_or_take SET is_su_status = 1, id_gt_status = 1
    WHERE   id_book = {id_book} 
        AND id_user = {id_user}
        AND id_gt_status = 2
        AND is_su_status = 2;
    ''')
    return conn.commit()


def cancel_rest_requests(conn, id_book, id_user):
    """
    Функция отменяет все заявки кроме заявки {id_user} пользователя
    1 - без статуса
    2 - рассмотрение
    3 - отклонена
    4 - удалена
    """
    cur = conn.cursor()
    cur.executescript(f'''
    UPDATE give_or_take SET is_su_status = 3
    WHERE   id_book = {id_book} 
        AND id_user != {id_user}
        AND id_gt_status = 2
        AND is_su_status = 2;
    ''')
    return conn.commit()
