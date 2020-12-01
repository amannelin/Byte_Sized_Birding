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