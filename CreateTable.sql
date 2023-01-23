--------------------------------------- green tables

DROP TABLE IF EXISTS country;
create table country
(
    id_country   INTEGER primary key AUTOINCREMENT,
    country_name varchar(255)
);

DROP TABLE IF EXISTS city;
create table city
(
    id_city    INTEGER primary key AUTOINCREMENT,
    city_name  varchar(255),
    id_country INTEGER,
    foreign key (id_country) references country (id_country)
);

DROP TABLE IF EXISTS address;
create table address
(
    id_address  INTEGER primary key AUTOINCREMENT,
    id_city     INTEGER,
    street      varchar(255),
--     coordinates varchar(255), --- поменять тип в зависимости от того как хранятся координаты
    foreign key (id_city) references city (id_city)
);

--------------------------------------- gray tables
DROP TABLE IF EXISTS author;
create table author
(
    id_author   INTEGER primary key AUTOINCREMENT,
    author_name varchar(255) not null
);

DROP TABLE IF EXISTS genre;
create table genre
(
    id_genre   INTEGER primary key AUTOINCREMENT,
    genre_name varchar(255) not null
);

DROP TABLE IF EXISTS language;
create table language
(
    id_language   INTEGER primary key AUTOINCREMENT,
    language_name varchar(255) not null
);

DROP TABLE IF EXISTS gt_status;
create table gt_status
(
    id_gt_status   INTEGER primary key AUTOINCREMENT,
    gt_status_name varchar(255) not null
);

DROP TABLE IF EXISTS us_status;
create table us_status
(
    id_us_status   INTEGER primary key AUTOINCREMENT,
    us_status_name varchar(255)  not null
);

DROP TABLE IF EXISTS photo;
-- create table photo
-- (
--     id_photo INTEGER primary key AUTOINCREMENT,
--     id_book  INTEGER not null ,
--     image    blob not null ,
--     foreign key (id_book) references book (id_book)
-- );

--------------------------------------- red tables

DROP TABLE IF EXISTS book_author;
create table book_author
(
    id_book_author INTEGER primary key AUTOINCREMENT,
    id_author      INTEGER  not null ,
    id_book        INTEGER  not null ,
    foreign key (id_author) references author (id_author),
    foreign key (id_book) references book (id_book_author)
);


--------------------------------------- yellow tables

DROP TABLE IF EXISTS book;
create table book
(
    id_book        INTEGER primary key AUTOINCREMENT,
    id_book_author INTEGER not null ,
    id_genre       INTEGER not null ,
    id_language    INTEGER not null ,
    title          varchar(255) not null ,
    description    varchar(255),
    price          DECIMAL(10, 2),
    foreign key (id_book_author) references book_author (id_book),
    foreign key (id_genre) references genre (id_genre),
    foreign key (id_language) references language (id_language)
);

DROP TABLE IF EXISTS shelf;
-- create table shelf
-- (
--     id_shelf   INTEGER primary key AUTOINCREMENT,
--     id_address INTEGER not null ,
--     foreign key (id_address) references address (id_address)
-- );

DROP TABLE IF EXISTS user;
create table user
(
    id_user INTEGER primary key AUTOINCREMENT,
    id_address INTEGER,
    login      varchar(255) not null ,
    password   varchar(255) not null ,
    messanger  varchar(255) not null ,
    -- дата регистрации
    -- дата рождения
    -- рейтинг
    foreign key (id_address) references address (id_address)
);

DROP TABLE IF EXISTS give_or_take;
create table give_or_take
(
    id_give_or_take INTEGER primary key AUTOINCREMENT,
    id_book      INTEGER not null,
    id_user      INTEGER,
--     id_shelf     INTEGER,
    id_gt_status INTEGER not null,
    is_su_status INTEGER not null,

    foreign key (id_book) references book (id_book),
    foreign key (id_user) references user (id_user),
--     foreign key (id_shelf) references shelf (id_shelf),
    foreign key (id_gt_status) references gt_status (id_gt_status),
    foreign key (is_su_status) references us_status (id_us_status)

);







