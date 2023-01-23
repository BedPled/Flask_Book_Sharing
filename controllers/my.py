from app import app, USER_ID
from flask import render_template
from models.search_bild import *
from models.my_books import *

import sqlite3
from models.search_bild import *
from jinja2 import Template

@app.route('/my', methods=['get'])
def my_books():
    conn = sqlite3.connect('identifier.sqlite')
    book_list = get_user_book(conn, USER_ID).values.tolist()

    html = render_template(
        'profile_my.html',
        book_list=book_list,
        USER_ID=USER_ID
    )

    conn.close()
    return html