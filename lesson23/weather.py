from dotenv import load_dotenv
from pprint import pprint
import requests
import os
load_dotenv()


def get_weather(city="San Diego"):

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={
        os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print("\n***Get Current Weather Conditions ***")

    city = input("\nPlease enter a city name: ")

    # Check for empty string or string with only spaces
    if not bool(city.strip()):
        city = "San Diego"

    weather_data = get_weather(city)

    print("\n")

    pprint(weather_data)
