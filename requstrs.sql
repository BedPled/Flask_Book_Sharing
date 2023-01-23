

-- два запроса на выборку для связанных таблиц с условиями и сортировкой;
------ найти все книги, по заданному автору (и отсортировать по названию)
select title, author_name from book
join book_author ba on ba.id_book = book.id_book_author
join author a on a.id_author = ba.id_author
where author_name = 'тут будет имя автора'
order by title;

------ найти вывести все книги по заданному жанру (и отсортировать по названию)
select title, genre_name from book
join genre g on g.id_genre = book.id_genre
where genre_name = 'название жанра'
order by title;



------ вывести кол-во книг, которые отдают пользователи. (группировать по городам)
select city_name, count(id_book) from give_or_take
                                 join user u on u.id_user = give_or_take.id_user
                                 join address a on a.id_address = u.id_address
                                 join city c on c.id_city = a.id_city
where id_gt_status == 1
group by city_name;



------ книги которые не отдаются и ищутся
 SELECT title
FROM book
WHERE id_book NOT IN (
    SELECT id_book FROM give_or_take
);

-- вывод книг со статусом моя книга
SELECT title, genre_name, author_name, language_name, price, description
FROM book
    join genre g on g.id_genre = book.id_genre
    join book_author ba on ba.id_book = book.id_book_author and book.id_book_author = ba.id_book
    join author a on a.id_author = ba.id_author
    join language l on l.id_language = book.id_language
    join give_or_take got on book.id_book = got.id_book
WHERE id_gt_status == 1 AND id_user == 2; -- моя книга




-- два запроса корректировки данных (обновление, добавление, удаление и пр)
insert into country (country_name)
values ('name');

insert into city (city_name, id_country)
VALUES ('city_name', 0); -- индекс страны вместо 0 или по названию