from app import app, USER_ID
from flask import render_template
from models.search_bild import *
from models.my_books import *

import sqlite3
from models.search_bild import *
from jinja2 import Template

@app.route('/request', methods=['get'])
def requests():
    conn = sqlite3.connect('identifier.sqlite')

    book_list = get_my_requests(conn, USER_ID).values.tolist()

    html = render_template(
        'profile_request.html',
        book_list=book_list,
        USER_ID=USER_ID
    )

    conn.close()
    return html