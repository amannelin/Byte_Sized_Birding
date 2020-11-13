import os
from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import connect_to_db
import crud
import data

from jinja2 import StrictUndefined
from datetime import datetime
import json
import urllib.request
import flickrapi
import requests
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

#TODO Flash message or other indication that something is happening during ebird request

@app.route('/ebird-call', methods=['GET', 'POST'])
def get_birds_by_loc():
    """use lat/long to make ebird call"""
    get_birds()
    try:
        if session['birds'][0]['comName']:
            return "The birds are flocking in!"
    except:
            return "Unable to find sightings for this location."
        

@app.route('/flickr-call')
def add_images():
    """use flickr api to add images to session birds"""
    for bird in session['birds']:
        bird_name = make_search_tag(bird)
        try:
            link = get_image_link(bird_name)
            bird['photo_1'] = link
        except:
            bird['photo_1'] = None
        session['birds'] = session['birds']

    return "Added Photos, please wait while we add bird songs"

    

@app.route('/xeno-canto-call')
def add_calls():
    """use xeno-canto api to add vocalizations to session birds"""
    for bird in session['birds']:
        bird_name = make_search_tag(bird)
        try:
            link = get_call_link(bird_name)
            bird['call_1'] = link
        except: 
            bird['call_1'] = None
    session['birds'] = session['birds']

    return "Added Songs!"


#FIXME : link issue!
#TODO : have bird list load first and add calls as they are returned. sloooooow


@app.route('/bird-list')
def show_bird_list():
    """display birding list"""
    

    return render_template("bird-list.html")

@app.route('/bird-details')
def show_details():
    """display more images, information, for bird from birding list"""

    return render_template("bird-details.html")

#TODO : details!

@app.route('/printable-list')
def make_list():
    """a printable version of the location-based list"""

    return render_template("printable-list.html")

#TODO : easy-peasy

@app.route('/bird-quiz')
def make_quiz():

    return render_template("bird-quiz.html")

#TODO : quiz! REACT?


def get_birds():
    """fetches 10 bird objects form ebird API"""

    lat = request.form.get("lat")
    lng = request.form.get("lng")
    session['birds'] = get_nearby_observations(KEY, lat, lng, dist=10, back=2, max_results=10)
    
    return session['birds']

def make_search_tag(bird):
    """gets bird common name from json and parses it into correct form for api calls"""

    bird_name = bird['comName']
    bird_name = bird_name.split()
    bird_name = "+".join(bird_name).lower()
    
    return bird_name


def get_image_link(bird_name):
    """use flicker api to get an image for a given bird"""
    
    flickr = flickrapi.FlickrAPI(FLICKR_API_KEY, FLICKR_API_SECRET)
    raw_json = flickr.photos.search(per_page='1', page='1', tags=bird_name, format='json')
    parsed = json.loads(raw_json.decode('utf-8'))
    image = parsed["photos"]["photo"][0]
    link = f"https://live.staticflickr.com/{image['server']}/{image['id']}_{image['secret']}_m.jpg"
    
    return link

def get_call_link(bird_name):
    """use xeno-canto api to get a vocalization for a given bird"""

    response = requests.get(f"https://www.xeno-canto.org/api/2/recordings?query={bird_name}+q:A+len_lt:20")
    url = response.json()['recordings'][0]['url']
    link = f"https:{url}/embed?simple=1"
    
    return link


        

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)