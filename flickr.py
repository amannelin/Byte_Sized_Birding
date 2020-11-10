import flickrapi
import json
import os

FLICKR_API_KEY = os.environ['FLICKR_API_KEY']
FLICKR_API_SECRET = os.environ["FLICKR_API_SECRET"]



def make_call_flickr(bird):
    flickr = flickrapi.FlickrAPI(FLICKR_API_KEY, FLICKR_API_SECRET)
    raw_json = flickr.photos.search(per_page='1', page='1', tags=bird, format='json')
    parsed = json.loads(raw_json.decode('utf-8'))

    return parsed


f'https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key={FLICKR_API_KEY}tags={bird}&per_page=3&page=1&format=json&nojsoncallback=1'

downy = {'photos': {'page': 1, 'pages': 11, 'perpage': 3, 'total': '31', 'photo': 
    [{'id': '48051425953', 'owner': '89103347@N00', 'secret': '08788be39d', 'server': '65535', 'farm': 66, 'title': 'Downy Woodpecker', 'ispublic': 1, 'isfriend': 0, 'isfamily': 0}, 
    {'id': '7109183181', 'owner': '63348497@N00', 'secret': 'd19e9e02ea', 'server': '7247', 'farm': 8, 'title': 'Dreaming of Walnuts', 'ispublic': 1, 'isfriend': 0, 'isfamily': 0}, 
    {'id': '4176627744', 'owner': '63348497@N00', 'secret': '4db80599a6', 'server': '4006', 'farm': 5, 'title': 'In the Shadows', 'ispublic': 1, 'isfriend': 0, 'isfamily': 0}]}, 'stat': 'ok'}

robin = {'photos': {'page': 1, 'pages': 7674, 'perpage': 3, 'total': '23020', 'photo': 
    [{'id': '50565911818', 'owner': '76617062@N08', 'secret': 'af847b42d3', 'server': '65535', 'farm': 66, 'title': "1.26163 Merle d'Amérique / Turdus migratorius migratorius / American Robin", 'ispublic': 1, 'isfriend': 0, 'isfamily': 0}, 
    {'id': '50560584242', 'owner': '95823068@N06', 'secret': '2b30c2e00d', 'server': '65535', 'farm': 66, 'title': 'Female American Robin', 'ispublic': 1, 'isfriend': 0, 'isfamily': 0}, 
    {'id': '50560475577', 'owner': '90721027@N06', 'secret': '4dd145c76c', 'server': '65535', 'farm': 66, 'title': 'A83I7357', 'ispublic': 1, 'isfriend': 0, 'isfamily': 0}]}, 'stat': 'ok'}

cardinal = {"photos":{"page":1,"pages":11425,"perpage":3,"total":"34275","photo":
    [{"id":"50563926652","owner":"54788905@N00","secret":"fdba9b31f8","server":"65535","farm":66,"title":"Cardinal rouge m\\u00e2le - Northern Cardinal - Beauce, PQ, Canada - 0854","ispublic":1,"isfriend":0,"isfamily":0},
    {"id":"50563322382","owner":"153179376@N05","secret":"f7787c6dd2","server":"65535","farm":66,"title":"Male Northern Cardinal","ispublic":1,"isfriend":0,"isfamily":0},
    {"id":"50563033662","owner":"186748160@N02","secret":"5f578cf9f4","server":"65535","farm":66,"title":"Northern cardinal in May - inquistive","ispublic":1,"isfriend":0,"isfamily":0}]},"stat":"ok"}

chickadee = { "photos": { "page": 1, "pages": "7809", "perpage": 3, "total": "23427", 
    "photo": [
      { "id": "50563052587", "owner": "186748160@N02", "secret": "8c32168165", "server": "65535", "farm": 66, "title": "Black-capped chickadee in November", "ispublic": 1, "isfriend": 0, "isfamily": 0 },
      { "id": "50562919116", "owner": "186748160@N02", "secret": "d91d6c86c6", "server": "65535", "farm": 66, "title": "Black-capped chickadee portrait", "ispublic": 1, "isfriend": 0, "isfamily": 0 },
      { "id": "50560780878", "owner": "38880314@N07", "secret": "4a2972372b", "server": "65535", "farm": 66, "title": "Rain & Snow", "ispublic": 1, "isfriend": 0, "isfamily": 0 }
    ] }, "stat": "ok" }

titmouse = {"photos":{"page":1,"pages":5370,"perpage":3,"total":"16109",
"photo":[{"id":"50564639112","owner":"18739614@N00","secret":"443f438a4e","server":"65535","farm":66,"title":"Tufted Titmouse","ispublic":1,"isfriend":0,"isfamily":0},
{"id":"50563341526","owner":"93410728@N03","secret":"bb0f8d4431","server":"65535","farm":66,"title":"Tufted Titmouse with berries","ispublic":1,"isfriend":0,"isfamily":0},
{"id":"50563169571","owner":"153179376@N05","secret":"a9b2ef0699","server":"65535","farm":66,"title":"Tufted Titmouse with peanut","ispublic":1,"isfriend":0,"isfamily":0}]},"stat":"ok"}

bluejay= {'photos': {'page': 1, 'pages': 20866, 'perpage': 3, 'total': '62596', 'photo': [{'id': '50586398073', 'owner': '130883876@N07', 'secret': 'be6a36b856', 'server': '65535', 'farm': 66, 'title': 'Morning visiter (Blue Jay)', 'ispublic': 1, 'isfriend': 0, 'isfamily': 0}, {'id': '50585856743', 'owner': '63348497@N00', 'secret': 'b7e2c8ff55', 'server': '65535', 'farm': 66, 'title': 'King of the Gazebo', 'ispublic': 1, 'isfriend': 0, 'isfamily': 0}, {'id': '50585735817', 'owner': '31279830@N00', 'secret': '7252bb5292', 'server': '65535', 'farm': 66, 'title': 'Blue Jay', 'ispublic': 1, 'isfriend': 0, 'isfamily': 0}]}, 'stat': 'ok'}

sandhill = {'photos': {'page': 1, 'pages': 43444, 'perpage': 1, 'total': '43444', 'photo': [{'id': '50587429782', 'owner': '140734051@N08', 'secret': 'c60568ccea', 'server': '65535', 'farm': 66, 'title': 'Канадский журавль, Antigone canadensis canadensis, Sandhill Crane', 'ispublic': 1, 'isfriend': 0, 'isfamily': 0}]}, 'stat': 'ok'}
def api_call(bird):

    request = f"https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key=6f3be1618e77f65b3101f277859b898b&tags={bird}&per_page=3&page=1&format=json&nojsoncallback=1"
    print(request)

    return request

def make_img_links(json):
    images = json["photos"]["photo"]
    
    for image in images:
        link = f"https://live.staticflickr.com/{image['server']}/{image['id']}_{image['secret']}_m.jpg"
        print(link)   
    return link

birds =    [{
        "comName": "Sandhill Crane",
        "howMany": 3,
        "lat": 44.92142,
        "lng": -93.30414,
        "locId": "L356105",
        "locName": "Lake Harriet",

    }]


# for bird in birds:
#     bird_name = bird['comName'].split()
#     bird = "+".join(bird_name).lower()
#     json = make_call_flickr(bird)
#     make_img_links(json)

def get_image_link(bird_name):
    """use flicker api to get an image for each bird in list"""
    flickr = flickrapi.FlickrAPI(FLICKR_API_KEY, FLICKR_API_SECRET)
    bird_name = bird_name.split()
    bird = "+".join(bird_name).lower()
    flickr = flickrapi.FlickrAPI(FLICKR_API_KEY, FLICKR_API_SECRET)
    raw_json = flickr.photos.search(per_page='1', page='1', tags=bird, format='json')
    parsed = json.loads(raw_json.decode('utf-8'))
    image = parsed["photos"]["photo"][0]
    link = f"https://live.staticflickr.com/{image['server']}/{image['id']}_{image['secret']}_m.jpg"
    return link


@app.route('/flickr-call')
def add_images():
    """use flickr api to add images to session birds"""
    
    for bird in session['birds']:
      bird_name = bird['comName']
      link = get_image_link(bird_name)
      bird['photo_1'] = link
    
    return jsonify(session['birds'])

get_image_link("Great-Horned Owl")
    







