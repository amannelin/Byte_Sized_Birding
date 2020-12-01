"""CRUD operations."""

from model import db, Bird, connect_to_db

def create_bird(speciesCode, sciName, comName, call1, searchTag):
    """Create and return a new bird."""

    bird = Bird(speciesCode=speciesCode, sciName=sciName, comName=comName, 
        call1=call1, searchTag=searchTag)

    db.session.add(bird)
    db.session.commit()

    return bird

def get_birds():
    """Return all birds."""

    return Bird.query.all()

def get_bird_by_code(speciesCode):
    """Return a bird by id."""

    return Bird.query.get(speciesCode)



if __name__ == '__main__':
    from server import app
    connect_to_db(app)