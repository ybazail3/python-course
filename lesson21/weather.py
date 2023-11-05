import requests
from dotenv import load_dotenv
import os
# pretty print for json text
from pprint import pprint

#
load_dotenv()

# Created a function named current weather


def current_weather():
    print("\n** Get current weather condition ***\n")

    # Created an object named city and we are asking the user for inout of the question Please enter a city name
    city = input("\nPlease enter a city name:\n")

    # Created an object using the format method and passing through the os & get env methods as well as calling the API KeY in our .env file * We want to keep our API KEYS a secret!!!!
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={
        os.getenv("API_KEY")}&q={city}&units=imperial'

    # we are printing the request url once we type in a city
    # print(request_url)

    # Created and object named weather_data where we are returning the request from open eather API and printing it into json format  and using pprint so it is more readable
    weather_data = requests.get(request_url).json()

    # pprint(weather_data)

    # Calling certain json data like the name of the city, the temp, what it feels like and the description from the API. We are doing this using the format method and using weather_data object then passing through the data we want.
    print(f"\nCurrent weather for {weather_data["name"]}")
    print(f"\nThe temp is {weather_data["main"]["temp"]}")
    print(f"\nFeels like {weather_data["main"]["feels_like"]} and {
          weather_data["weather"][0]["description"]}.")


# If this fles name is __main__ fun the function current_weather()
if __name__ == "__main__":
    # Calling the function curent_weather
    current_weather()
