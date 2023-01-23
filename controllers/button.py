import json

from app import app, USER_ID
from flask import render_template, request
from models.search_bild import *
from models.my_books import *
import sqlite3


@app.route('/button', methods=['get'])
def button():
    conn = sqlite3.connect('identifier.sqlite')

    book_id = request.args.get('book_id')
    su_status_id = request.args.get('btn')
    gt_status_id = request.args.get('gt')


    if gt_status_id == 2 and su_status_id == 1:
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

    set_book_us_status(conn, USER_ID, book_id, su_status_id)
    set_book_gt_status(conn, USER_ID, book_id, gt_status_id)


    if su_status_id == "4" or gt_status_id == "1":
        cancel_rest_requests(conn, book_id, USER_ID)

    conn.close()

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
