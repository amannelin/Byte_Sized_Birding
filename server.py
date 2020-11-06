import os
from flask import (Flask, render_template, request, flash, session,
                   redirect)
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
FLICKER_SECRET = os.environ["FLICKR_API_SECRET"]
GMAPS_API_KEY = os.environ["GMAPS_API_KEY"]

app = Flask(__name__)


@app.route('/')
def show_homepage():
    """display homepage"""

    return render_template('home.html')

@app.route('/bird-list')
def show_bird_list():
    """display birding list"""


    return render_template('bird_list.html')

# @app.route('/get-birds.json')
# def get_birds():
#     location = request.args.get('results')
#     console.log('results')
#     # birds.json = get_nearby_observations(KEY, lat, lng, dist=10, back=2, max_results=10)

#     return birdsearch.json


# def make_call_flickr(bird):
#     flickr = flickrapi.FlickrAPI(FLICKR_API_KEY, FLICKR_API_SECRET)
#     raw_json = flickr.photos.search(per_page='3', page='1', tags='downy+woodpeckr', format='json')
#     json = json.loads(raw_json.decode('utf-8'))
#     print(json)

#     return json

# print(json.dumps(home, indent=4, sort_keys=True))

# def make_img_links(json):
#     images = json["photos"]["photo"]
    
#     for image in images:
#         link = f"https://live.staticflickr.com/{image['server']}/{image['id']}_{image['secret']}_s.jpg"
#         print(link)   
#     return link


# print(json.dumps(home, indent=4, sort_keys=True))






if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)