import os
from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import connect_to_db
import crud
import data

from jinja2 import StrictUndefined
# import googlemaps
from datetime import datetime
import json
import urllib.request
import flickrapi
from ebird.api import get_nearby_observations, get_species_observations, get_nearby_notable
KEY = os.environ['API_KEY']
FLICKR_API_KEY = os.environ['FLICKR_API_KEY']
FLICKR_API_SECRET = os.environ["FLICKR_API_SECRET"]
GMAPS_API_KEY = os.environ["GMAPS_API_KEY"]

app = Flask(__name__)
app.secret_key = b'show/me?the#birds!'


@app.route('/')
def show_homepage():
    """display homepage"""

    return render_template('home.html')

@app.route('/ebird-call', methods=['GET', 'POST'])
def get_birds_by_loc():
    """use lat/long to make ebird call"""
    session['birds'] = get_birds()
    # for bird in session['birds']:
    #     get_image_link(bird)

    return session['birds'][0]['comName']


@app.route('/bird-list')
def show_bird_list():
    """display birding list"""


    return render_template('bird_list.html')


def get_birds():
    """fetches 10 bird objects form ebird API"""

    lat = request.form.get("lat")
    lng = request.form.get("lng")
    birds = get_nearby_observations(KEY, lat, lng, dist=10, back=2, max_results=10)
    # birds = jsonify(birds)

    return birds

def get_image_link(bird):
    """use flicker api to get an image for each bird in list"""
    flickr = flickrapi.FlickrAPI(FLICKR_API_KEY, FLICKR_API_SECRET)
    bird_name = "Blue Jay".split()
    bird_name = "+".join(bird_name).lower
    raw_json = flickr.photos.search(per_page='1', page='1', tags='{bird_name}', format='json')
    # parsed = json.loads(raw_json.decode('utf-8'))
    # image= parsed['photos']['photo']
    # link = f"https://live.staticflickr.com/{image['server']}/{image['id']}_{image['secret']}_m.jpg"
  

    return raw_json

# def get_bird_ids(birds):
#     """returns bird ids for all bird objects in birds"""
#     ids = []
#     for bird in birds:
#         id = bird["speciesCode"]
#         ids.append(id)

#     return ids

# def make_bird_div(birds):
#     for bird in birds:

        

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)