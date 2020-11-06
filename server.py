from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined
import googlemaps
from datetime import datetime
import json
import urllib.request



app = Flask(__name__)


@app.route('/')
def show_homepage():
    """display homepage"""

    return render_template('home_test.html')

@app.route('/birding_list')
def show_bird_list():
    """display birding list"""

    return render_template('bird_list.html')

# def geocode(address):
#     gmaps = googlemaps.Client(key='AIzaSyAUAbrtBxOl8_xUzqcSYfz88dVmthTSwIk')
#     geocode_result = gmaps.geocode(f'{address}')




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)