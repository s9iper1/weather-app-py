import json

import requests as requests


def get_weather_from_latlng(lat, lng):
    url = f'http://api.weatherstack.com/current?access_key=weather_stack_api_key&query= {lat} , {lng}&units=m'
    response = requests.get(url)
    data = json.loads(response.content)
    message = f'There is {str(data["current"]["temperature"])} degree outside and it feels ' \
              f'like {str(data["current"]["feelslike"])} degree and ' \
              f' {str(data["current"]["precip"])} % chance of rain and humidity ' \
              f'is {str(data["current"]["humidity"])} %'
    return message
