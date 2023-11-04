import requests
from dotenv import load_dotenv
import os

load_dotenv()


def current_weather():
    print("\n** Get current weather condition ***\n")

    city = input("\nPlease enter a city name:\n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={
        os.getenv("API_KEY")}&q={city}&units=imperial'

    print(request_url)

    weather_data = requests.get(request_url).json()

    print(weather_data)


current_weather()
