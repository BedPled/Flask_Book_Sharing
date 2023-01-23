from app import app, USER_ID
from flask import render_template, request
import sqlite3
from models.search_bild import *
from models.my_books import *

@app.route('/', methods=['get'])
def index():
    conn = sqlite3.connect('identifier.sqlite')

    country_list = [x for x in get_all_country(conn).values.tolist()]
    city_list = [x for x in get_all_city(conn).values.tolist()]
    genre_list = [x[1] for x in get_all_genre(conn).values.tolist()]
    language_list = [x[1] for x in get_all_language(conn).values.tolist()]


    if request.values.get('city') is not None:
        book_list = [x for x in get_book_by_param(conn,
                                              request.values.get('city'),
                                              request.values.get('genre'),
                                              request.values.get('lang'),
                                              request.values.get('author'),
                                              request.values.get('title')).values.tolist()]
    else:
        book_list = [x for x in get_book_by_param(conn,
                                                  "",
                                                  "",
                                                  "",
                                                  "",
                                                  "").values.tolist()]
    html = render_template(
        'index.html',
        country_list=country_list,
        city_list=city_list,
        genre_list=genre_list,
        language_list=language_list,
        book_list=book_list,
        USER_ID=USER_ID
    )


    conn.close()
    return html
