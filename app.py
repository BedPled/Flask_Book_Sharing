from flask import Flask

app = Flask(__name__)

USER_ID = 1
import controllers.index
import controllers.my
import controllers.request
import controllers.give
import controllers.button
import controllers.req_button
import controllers.give_button
