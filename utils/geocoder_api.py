import json
import urllib.parse

import requests


async def get_lat_lng_from_address(address):
    url = 'https://api.mapbox.com/geocoding/v5/mapbox.places/' + urllib.parse.quote(
        address) + '.json?access_token=access_token&limit=1'
    response = requests.get(url)
    data = json.loads(response.content)
    print(data)
    lat = data["features"][0]["center"][0]
    lng = data["features"][0]["center"][1]
    return lat, lng
