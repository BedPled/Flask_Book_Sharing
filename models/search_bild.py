import pandas as pandas

def get_all_country(conn):
    return pandas.read_sql('''
        SELECT *
        FROM country
    ''', conn)


def get_all_city(conn):
    return pandas.read_sql('''
        SELECT *
        FROM city
    ''', conn)


def get_city(conn, id_country):
    return pandas.read_sql('''
        SELECT *
        FROM city
        WHERE id_country = :country
    ''', conn, params={"country": id_country})


def get_all_genre(conn):
    return pandas.read_sql('''
        SELECT *
        FROM genre 
    ''', conn)


def get_all_language(conn):
    return pandas.read_sql('''
        SELECT *
        FROM language 
    ''', conn)
