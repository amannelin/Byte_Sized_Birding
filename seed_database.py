"""Script to seed database."""

import os
import json
from datetime import datetime

import crud
import model
import server

os.system('dropdb locate_birds')
os.system('createdb locate_birds')

model.connect_to_db(server.app)
model.db.create_all()

# with open('data/birds.json') as b:
#     bird_data = json.loads(b.read())

# birds_in_db = []
# for bird in bird_data:
#     speciesCode, sciName, comName, call1, searchTag = (bird['speciesCode'],
#         bird['sciName'],
#         bird['comName'],
#         bird['call1'],
#         bird['searchTag'])

#     db_bird = crud.create_bird(speciesCode, sciName, comName, song1, searchTag)
#     birds_in_db.append(db_bird)
