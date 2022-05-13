import asyncio

import utils.geocoder_api
import utils.api_helper


async def main():
    entered_location = input("Enter your location > \n")
    if entered_location.strip() != "":
        task = asyncio.create_task(utils.geocoder_api.get_lat_lng_from_address(entered_location))
        await task
        lat, lng = task.result()

        data = utils.api_helper.get_weather_from_latlng(lat, lng)
        print(data)

        # here we call the geocoderapi to get lat lng
    else:
        print("please enter a valid location")


asyncio.run(main())
