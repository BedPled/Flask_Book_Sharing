import json

from app import app, USER_ID
from flask import render_template, request
from models.my_books import *
import sqlite3


@app.route('/req_button', methods=['get'])
def req_button():
    conn = sqlite3.connect('identifier.sqlite')

    book_id = request.args.get('book_id')
    req_list = [x for x in check_request(conn, book_id, USER_ID).values.tolist()]

    if not req_list:
        request_button(conn, book_id, USER_ID)

    conn.close()

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
