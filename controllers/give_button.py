import json

from app import app, USER_ID
from flask import render_template, request
from models.my_books import *
import sqlite3


@app.route('/give_button', methods=['get'])
def give_button():
    conn = sqlite3.connect('identifier.sqlite')

    book_id = request.args.get('book_id')
    su_status = request.args.get('su_status')
    user_id = request.args.get('user_id')

    print(su_status)

    if su_status == "1": # приняли запрос
        print(su_status)
        set_book_gt_status(conn, USER_ID, book_id, 1)
        set_book_us_status(conn, USER_ID, book_id, 4)
        accept_and_cancel_rest_requests(conn, book_id, user_id)


    if su_status == "3": # отказали
        print(su_status)
        set_book_us_status(conn, user_id, book_id, 3)

    conn.close()

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
