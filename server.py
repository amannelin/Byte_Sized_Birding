import os
from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from jinja2 import StrictUndefined
from datetime import datetime
import json
import urllib.request
import requests
import random

import crud
from model import connect_to_db
import data

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

    return render_template('map.html')

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

def get_birds():
    """fetches 12 bird objects from ebird API"""

    lat = request.form.get("lat")
    lng = request.form.get("lng")
    session['birds'] = get_nearby_observations(KEY, lat, lng, dist=10, back=2, max_results=12)
    
    return session['birds']
        

#TODO:  stay on home page if no sightings     


@app.route('/flickr-call')
def add_images():
    """use flickr api to add images to session birds"""
    for bird in session['birds']:
        bird_name = make_search_tag(bird)
        try:
            link = get_image_link(bird["searchTag"])
            bird['photo1'] = link
        except:
            bird['photo1'] = None
        session['birds'] = session['birds']

    return "Added Photos, please wait while we add bird songs"

def make_search_tag(bird):
    """gets bird common name from json and parses it into correct form for api calls"""

    bird_name = bird['comName']
    bird_name = bird_name.split()
    bird_name = "+".join(bird_name).lower()
    bird['searchTag'] = bird_name

    return bird_name


def get_image_link(bird_name):
    """use flicker api to get an image for a given bird"""
    
    flickr = flickrapi.FlickrAPI(FLICKR_API_KEY, FLICKR_API_SECRET)
    raw_json = flickr.photos.search(per_page='1', page='1', tags=bird_name, format='json')
    parsed = json.loads(raw_json.decode('utf-8'))
    image = parsed["photos"]["photo"][0]
    link = f"https://live.staticflickr.com/{image['server']}/{image['id']}_{image['secret']}_m.jpg"
    
    return link

#TODO: image attribution!

    

@app.route('/xeno-canto-call')
def add_calls():
    """use xeno-canto api to add vocalizations to session birds"""

    for bird in session['birds']:
        in_db = crud.get_bird_by_code(bird['speciesCode'])
        if in_db:
            bird['call1']=in_db.call1

        else:
            bird_name = bird['searchTag']
            link = get_call_link(bird_name)
            bird['call1'] = link

        session['birds'] = session['birds']

    return "Added Songs!"


def get_call_link(bird_name):
    """use xeno-canto api to get a vocalization for a given bird"""

    response = requests.get(f"https://www.xeno-canto.org/api/2/recordings?query={bird_name}+q:A+len_lt:20")
    try:
        url = response.json()['recordings'][0]['url']
        link = f"https:{url}/embed?simple=1"
    except:
        link = None
    
    return link

#FIXME : link issue!


@app.route('/save-birds')
def save_birds_to_db():
    """add birds to database for improved performance"""

    for bird in session['birds']:
        in_db = crud.get_bird_by_code(bird['speciesCode'])
        if in_db:
            pass
        else:
            speciesCode=bird['speciesCode']
            sciName=bird['sciName']
            comName=bird['comName']
            call1=bird['call1']
            searchTag = bird['searchTag']
            crud.create_bird(speciesCode, sciName, comName, call1, searchTag)
    
    return "successfully added new birds to database!"


@app.route('/bird-list')
def show_bird_list():
    """display birding list"""
    

    return render_template("bird-list.html")


@app.route('/bird-details/<speciesCode>')
def show_details(speciesCode):
    """display more images, information, for bird from birding list"""

    bird = crud.get_bird_by_code(speciesCode)
    links = get_three_images(bird.searchTag)
    bird.photo2=links[1]
    bird.photo3=links[2]
    bird.photo4=links[3]

    return render_template("bird-details.html", bird=bird)

def get_three_images(bird_name):
    """use flicker api to get three images for bird detail page"""
    
    flickr = flickrapi.FlickrAPI(FLICKR_API_KEY, FLICKR_API_SECRET)
    raw_json = flickr.photos.search(per_page='5', page='1', tags=bird_name, format='json')
    parsed = json.loads(raw_json.decode('utf-8'))
    images = parsed['photos']['photo']
    links = []
    for image in images:
        link = f"https://live.staticflickr.com/{image['server']}/{image['id']}_{image['secret']}_m.jpg"
        links.append(link)

    return links



@app.route('/printable-list')
def make_list():
    """a printable version of the location-based list"""

    return render_template("printable-list.html")


@app.route('/bird-quiz')
def make_quiz():
    """a quiz on 10 species from the birding list"""

    return render_template("bird-quiz.html")


@app.route('/quiz-data.api')
def make_questions():
    """local api for quiz data json"""
    
    q_and_a = make_quiz_data()
    

    return jsonify(q_and_a)

def make_quiz_data():
    """Make an array containing Question and Answer possiblities"""
    
    birds = session['birds']
    quiz = [{"question": "Welcome", "answers":[{"name":"Start Quiz!", "isCorrect": False}]}]
    
    x = 0
   
    for bird in birds:
        if x < 10:
            r = random.sample([i for i in range(0,11) if i != x], k=3)
            answers = [{"name": bird['comName'], "isCorrect": True}, 
                        {"key": 1, "name": birds[r[0]]['comName'], "isCorrect": False}, 
                        {"key": 2, "name": birds[r[1]]['comName'], "isCorrect": False}, 
                        {"key": 3, "name":birds[r[2]]["comName"], "isCorrect":False}]
            answers_shuffled = random.shuffle(answers)
            x = x + 1
            quiz.append({"question": bird['photo1'], "answers": answers})
    return quiz

@app.route("/about")
def about_page():

    return render_template("about.html")
        

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)