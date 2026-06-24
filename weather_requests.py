import requests
from pprint import pprint

WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather?"

latitude = 51.5933
longitude = 0.2000
with open("weather_api_key") as file:
    api_key = file.readline().strip()

response = requests.get(WEATHER_ENDPOINT + f"lat={latitude}&lon={longitude}&appid={api_key}")

print(response.status_code)

if response.status_code == 200:
    weather = response.json()
    pprint(weather)
