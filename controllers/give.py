from app import app, USER_ID
from flask import render_template

import sqlite3

from models.my_books import get_my_gives
from models.search_bild import *
from jinja2 import Template

@app.route('/give', methods=['get'])
def give_books():
    conn = sqlite3.connect('identifier.sqlite')

    book_list= [x for x in get_my_gives(conn, USER_ID).values.tolist()]

    html = render_template(
        'profile_give.html',
        USER_ID=USER_ID,
        book_list=book_list
    )

    conn.close()
    return html