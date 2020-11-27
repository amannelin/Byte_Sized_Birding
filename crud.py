"""CRUD operations."""

from model import db, Bird, Location, Search, connect_to_db
from random import choice


#TODO update this and Model

def create_bird(speciesCode, sciName, comName, call1, searchTag):
    """Create and return a new bird."""

    bird = Bird(speciesCode=speciesCode, sciName=sciName, comName=comName, 
        call1=call1, searchTag=searchTag)

    db.session.add(bird)
    db.session.commit()

    return bird

def create_location(address, latitude, longitude, 
                    radius, time, num_results):
    """Create and return a new location."""

    location = Location(address=address, latitude=latitude, longitude=longitude,
                        radius=radius, time=time, num_results=num_results)

    db.session.add(location)
    db.session.commit()

# def create_search(location_id, bird_id):
#     """Create and return a new search."""

#     search = Search(location_id=location_id, bird_id=bird_id)

#     db.session.add(location)
#     db.session.commit()

def get_birds():
    """Return all birds."""

    return Bird.query.all()

def get_bird_by_code(speciesCode):
    """Return a bird by id."""

    return Bird.query.get(speciesCode)

# def make_quiz_data():
#     """Make an array containing Question and Answer possiblities"""
#     birds = session['birds']
#     quiz = []
#     for bird in birds:
#         q_a = {}
#         q = "question":{"text":bird['photo1']}
#         a = "answer": {"name": bird['comName'], "is_correct": True},
#                         {"name": "chickadee". "is_correct": False}
#         quiz.append(q,a)
#     return quiz_data

if __name__ == '__main__':
    from server import app
    connect_to_db(app)