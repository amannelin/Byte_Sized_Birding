import os
import json
from ebird.api import get_nearby_observations, get_species_observations, get_nearby_notable
KEY = os.environ['API_KEY']

def birds(location):
    for dict in location:
        print(dict['comName'])

def species(bird):
    for dict in bird:
            print(dict['locName'])

def find_birds(nearby):
    for dict in nearby:
        print((dict['comName']))
        print((dict['locName']))


home = get_nearby_observations(KEY, 44.93, -93.26, dist=10, back=2, max_results=10)
print(json.dumps(home, indent=4, sort_keys=True))

chickadee_hollow = get_nearby_observations(KEY, 46.12, -92.43, dist=10, back=14, max_results=10)
# print(json.dumps(chickadee_hollow, indent=4, sort_keys=True))

sandhill = get_species_observations(KEY, 'sancra', 'US-MN')
#print(sandhill)
#species(sandhill)

kestrel = get_species_observations(KEY, 'amekes', 'US-MN')
#species(kestrel)

fun = get_nearby_notable(KEY, 44.93, -93.26, dist=10)
# find_birds(fun)






