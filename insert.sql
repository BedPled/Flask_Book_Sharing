INSERT INTO country (country_name)
VALUES ('Россия'),
       ('Казахстан'),
       ('Беларусь');

INSERT INTO city (city_name, id_country)
VALUES ('Москва', '1'),
       ('Новосибирск', '1'),
       ('Владивосток', '1'),

       ('Астана', '2'),
       ('Караганда', '2'),
       ('Алматы', '2'),

       ('Минск', '3'),
       ('Барановичи', '3'),
       ('Могилёв', '3');

INSERT INTO address (id_city, street)
VALUES
    (1,'Пушкина'),
    (1,'Охотничья'),
    (1,'Ленина'),
    (2,'Маркса'),
    (2,'Киевская'),
    (2,'Красный проспект'),
    (3,'Светланская'),
    (3,'Постышева'),
    (3,'Океанский проспект');

INSERT INTO genre (genre_name)
VALUES
    ('Детектив'),
    ('Роман'),
    ('Приключения'),
    ('Фантастика');

INSERT INTO language (language_name)
VALUES
    ('Русский'),
    ('Английский');

INSERT INTO user (id_address, login, password, messanger)
VALUES
    (1,1,1,'1'),
    (2,2,2,'2'),
    (3,3,3,'3'),
    (4,4,4,'4'),
    (5,5,5,'5'),
    (6,6,6,'6'),
    (7,7,7,'7'),
    (8,8,8,'8'),
    (9,9,9,'9');

INSERT INTO author (author_name)
VALUES
    ('Сапольский'),
    ('Пушкин'),
    ('Фейман'),
    ('Докинз'),
    ('Толстой');


INSERT INTO book_author (id_author, id_book) VALUES (1, 1);
INSERT INTO book_author (id_author, id_book) VALUES (2, 2);
INSERT INTO book_author (id_author, id_book) VALUES (3, 3);


INSERT INTO book (id_book_author, id_genre, id_language, title, description, price) VALUES (1, 1, 1, 'Книга 1', 'Очень хорошая книга', 1.00);
INSERT INTO book (id_book_author, id_genre, id_language, title, description, price) VALUES (2, 2, 2, 'Книга 2', 'Вторая очень хорошая книга', 2.00);
INSERT INTO book (id_book_author, id_genre, id_language, title, description, price) VALUES (3, 3, 2, 'Книга 3', 'Не очень хорошая книга', 3.00);


INSERT INTO gt_status (gt_status_name) VALUES ('моя');
INSERT INTO gt_status (gt_status_name) VALUES ('отдаю');

INSERT INTO us_status (us_status_name)
VALUES  ('без статуса'),
        ('рассмотрение'),
        ('отклонена'),
        ('удалена');

INSERT INTO give_or_take (id_book, id_user, id_gt_status, is_su_status)
VALUES
        (1, 1, 1, 1),
        (2, 2, 1, 1),
        (3, 2, 1, 1);

