"""CRUD operations."""

from model import db, Bird, Location, Search, connect_to_db


def create_bird(bird_id, scientific_name, common_name, photo_1, song_1, ebird_page):
    """Create and return a new bird."""

    bird = Bird(bird_id=bird_id, scientific_name=scientific_name, common_name=common_name, 
        photo_1=photo_1, call_1=call_1, ebird_page=ebird_page)

    db.session.add(bird)
    db.session.commit()

    return bird

def create_location(country, state, city, latitude, longitude, 
                    radius, time, num_results):
    """Create and return a new location."""

    location = Location(country=country, state=state,
                        city=city, latitude=latitude, longitude=longitude,
                        radius=radius, time=time, num_results=num_results)

    db.session.add(location)
    db.session.commit()

def create_search(location_id, bird_id):
    """Create and return a new search."""

    search = Search(location_id=location_id, bird_id=bird_id)

    db.session.add(location)
    db.session.commit()

def get_birds():
    """return all birds"""

    return Bird.query.all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)