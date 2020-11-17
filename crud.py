"""CRUD operations."""

from model import db, Bird, Location, Search, connect_to_db


def create_bird(speciesCode, sciName, comName, photo1, call1, searchTag):
    """Create and return a new bird."""

    bird = Bird(speciesCode=speciesCode, sciName=sciName, comName=comName, 
         photo1=photo1, call1=call1, searchTag=searchTag)

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



if __name__ == '__main__':
    from server import app
    connect_to_db(app)