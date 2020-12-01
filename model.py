from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""Models for birding list app"""

class Bird(db.Model):
    """A bird."""

    __tablename__ = 'birds'

    #will use 6-letter species abbreviation as primary key
    speciesCode = db.Column(db.String, primary_key=True)
    sciName = db.Column(db.String, unique = True, nullable=False)
    comName = db.Column(db.String)
    searchTag = db.Column(db.String)
    call1 = db.Column(db.String)

    # location_birds = a list of location search objects

    def __repr__(self):
        return f'<Bird bird_id={self.speciesCode} name={self.comName}>'

class Location(db.Model):
    """location data"""

    __tablename__ = "locations"

    location_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    location_name = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    radius = db.Column(db.Integer, default=25)
    time = db.Column(db.Integer, default=14)
    num_results = db.Column(db.Integer, default=12)

    # location_birds = a list of location search objects

    def __repr__(self):
        return f'<Location location_id={self.location_id}, {self.latitude}, {self.longitude}>'
    
class Search(db.Model):
    """A location search"""

    __tablename__= "searches"

    search_id = db.Column(db.Integer, autoincrement=True, 
                        primary_key=True)
    location_id = db.Column(db.Integer, 
                db.ForeignKey('locations.location_id'))
    bird_id = db.Column(db.String, db.ForeignKey('birds.speciesCode'))

    bird = db.relationship('Bird', backref='location_birds')
    location =db.relationship('Location', backref='location_birds')

    def __repr__(self):
        return f'<Search id={self.location_birds_id}>'

def connect_to_db(flask_app, db_uri='postgresql:///locate_birds', echo=False):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    connect_to_db(app)