import googlemaps
from datetime import datetime
import json
import urllib.request

gmaps = googlemaps.Client(key=GMAPS_API_KEY)

# Geocoding an address
address = '3804 Elliot Ave, Minneapolis'
geocode_result = gmaps.geocode(f'{address}')

# print(geocode_result)

j = [{'address_components': [{'long_name': '3804', 'short_name': '3804', 'types': ['street_number']}, {'long_name': 'Elliot Avenue', 'short_name': 'Elliot Ave.', 'types': ['route']}, {'long_name': 'Bancroft', 'short_name': 'Bancroft', 'types': ['neighborhood', 'political']}, {'long_name': 'Minneapolis', 'short_name': 'Minneapolis', 'types': ['locality', 'political']}, {'long_name': 'Hennepin County', 'short_name': 'Hennepin County', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Minnesota', 'short_name': 'MN', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}, {'long_name': '55407', 'short_name': '55407', 'types': ['postal_code']}, {'long_name': '2616', 'short_name': '2616', 'types': ['postal_code_suffix']}], 'formatted_address': '3804 Elliot Ave., Minneapolis, MN 55407, USA', 'geometry': {'bounds': {'northeast': {'lat': 44.933933, 'lng': -93.2614141}, 'southwest': {'lat': 44.93386080000001, 'lng': -93.261617}}, 'location': {'lat': 44.93390300000001, 'lng': -93.26152540000001}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 44.9352458802915, 'lng': -93.26016656970849}, 'southwest': {'lat': 44.9325479197085, 'lng': -93.26286453029151}}}, 'place_id': 'ChIJ07LVOd4n9ocRp5jKJ_yDVrA', 'types': ['premise']}]


result = [{'address_components': 
[{'long_name': '3520', 'short_name': '3520', 'types': ['street_number']}, 
{'long_name': 'Elliot Avenue', 'short_name': 'Elliot Ave.', 'types': ['route']}, 
{'long_name': 'Powderhorn Park', 'short_name': 'Powderhorn Park', 'types': ['neighborhood', 'political']}, 
{'long_name': 'Minneapolis', 'short_name': 'Minneapolis', 'types': ['locality', 'political']}, 
{'long_name': 'Hennepin County', 'short_name': 'Hennepin County', 'types': ['administrative_area_level_2', 'political']}, 
{'long_name': 'Minnesota', 'short_name': 'MN', 'types': ['administrative_area_level_1', 'political']}, 
{'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}, 
{'long_name': '55407', 'short_name': '55407', 'types': ['postal_code']}, 
{'long_name': '2129', 'short_name': '2129', 'types': ['postal_code_suffix']}], 
'formatted_address': '3520 Elliot Ave., Minneapolis, MN 55407, USA', 'geometry': 
{'bounds': {'northeast': 
{'lat': 44.9388662, 'lng': -93.26145869999999}, 
'southwest': {'lat': 44.9387925, 'lng': -93.2615996}}, 
'location': {'lat': 44.9388225, 'lng': -93.26152540000001}, 
'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 44.9401783302915, 'lng': -93.26018016970848}, 'southwest': {'lat': 44.9374803697085, 'lng': -93.2628781302915}}}, 'place_id': 'ChIJiWUsbuEn9ocRFfiOJcV9FPc', 'types': ['premise']}]

lat = result[0]['geometry']['location']['lat']
lng = result[0]['geometry']['location']['lng']
address = result[0]['formatted_address']

# print(lat)

