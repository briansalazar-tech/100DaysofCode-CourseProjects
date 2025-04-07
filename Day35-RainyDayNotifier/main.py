import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

URL = "https://api.openweathermap.org/data/2.5/forecast"
TWILIO_ACCOUNT = os.getenv("TWILIO_ACCOUNT"),
TWILIO_AUTH = os.getenv("TWILIO_AUTH"),

parameters = {
    "lat": 34.05223000,
    "lon": -118.24368000,
    "appid": os.getenv("OPENWEATHER_API_KEY"),
    "cnt": 4, # Limits to 12 hours of data

}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()
weather_data = response.json()

# USE FOR TESTING: Inserted id of 500 to ensure incliment weather is detected
# weather_data = {'cod': '200', 'message': 0, 'cnt': 4, 'list': [{'dt': 1744048800, 'main': {'temp': 293.97, 'feels_like': 293.2, 'temp_min': 293.97, 'temp_max': 295.21, 'pressure': 1019, 'sea_level': 1019, 'grnd_level': 1000, 'humidity': 42, 'temp_kf': -1.24}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 2.2, 'deg': 158, 'gust': 1.83}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-04-07 18:00:00'}, {'dt': 1744059600, 'main': {'temp': 295.5, 'feels_like': 294.68, 'temp_min': 295.5, 'temp_max': 298.56, 'pressure': 1018, 'sea_level': 1018, 'grnd_level': 998, 'humidity': 34, 'temp_kf': -3.06}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 3.58, 'deg': 205, 'gust': 2.01}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-04-07 21:00:00'}, {'dt': 1744070400, 'main': {'temp': 295.67, 'feels_like': 294.84, 'temp_min': 295.67, 'temp_max': 296.52, 'pressure': 1017, 'sea_level': 1017, 'grnd_level': 997, 'humidity': 33, 'temp_kf': -0.85}, 'weather': [{'id': 501, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 4.65, 'deg': 230, 'gust': 3.15}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-04-08 00:00:00'}, {'dt': 1744081200, 'main': {'temp': 292.3, 'feels_like': 291.32, 'temp_min': 292.3, 'temp_max': 292.3, 'pressure': 1017, 'sea_level': 1017, 'grnd_level': 997, 'humidity': 40, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 2}, 'wind': {'speed': 1.95, 'deg': 214, 'gust': 2.38}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2025-04-08 03:00:00'}], 'city': {'id': 5368361, 'name': 'Los Angeles', 'coord': {'lat': 34.0522, 'lon': -118.2437}, 'country': 'US', 'population': 3792621, 'timezone': -25200, 'sunrise': 1744032698, 'sunset': 1744078676}}

# Codes less than 700 indicate inclement weather
for hour in weather_data["list"]:
     
    condition_code = (hour["weather"][0]["id"])
    if condition_code < 700:
        print("Inclement Weather. Sending message...")

        # NOTE: Due to changes, unable to use Twilio's free trial number as number requires verification in order to send toll-free message.
        # Alternatively, can use smtplib to send email
        client = Client(TWILIO_ACCOUNT, TWILIO_AUTH)

        message = client.messages.create(
        from_="+18775638931",
        body="It's going to rain today. Remember to bring an umbrella! ☔",
        to="+18777804236"
        )

        print(message.status)    
        break
