from config import MAP_API_KEY
import json, urllib.request

MAPBOX_BASE_URL = 'https://api.mapbox.com/geocoding/v5/mapbox.places'
MAPBOX_TOKEN = MAP_API_KEY

def make_mapbox_url(coords:tuple):
    url = f'{MAPBOX_BASE_URL}/{coords[1]},{coords[0]}.json?access_token={MAPBOX_TOKEN}&types=poi'

    return url

def get_json(url:str):
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
    
    return response_data

def get_address(response_data):
    try:
        address = response_data['features'][0]['place_name']
        return address
    except:
        address = None

def address_from_coords(coords):
    url = make_mapbox_url(coords)
    data = get_json(url)
    address = get_address(data)

    return address

