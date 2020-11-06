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

with open('data/birds.json') as b:
    bird_data = json.loads(b.read())

birds_in_db = []
for bird in bird_data:
    bird_id, scientific_name, common_name, photo_1, song_1, ebird_page =
        (bird['bird_id'],
        bird['scientific_name'],
        bird['common_name'],
        bird['photo_1'],
        bird['song_1'],
        bird['ebird_page'])

    db_bird = crud.create_bird(bird_id, scientific_name, common_name, photo_1, song_1, ebird_page)
    birds_in_db.append(db_bird)

locations