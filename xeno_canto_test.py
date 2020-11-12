import json
import xenocanto
import requests

def get_call_link(bird_name):
    """use xeno-canto api to get a vocalization for each bird in list"""
    response = requests.get(f"https://www.xeno-canto.org/api/2/recordings?query={bird_name}+q:A")
    url = response.json()['recordings'][0]['url']
    link = f"<iframe src='https:{url}/embed?simple=1' scrolling='no' frameborder='0' width='340' height='115'></iframe>"
    return link


print(get_call_link("barred+owl"))

