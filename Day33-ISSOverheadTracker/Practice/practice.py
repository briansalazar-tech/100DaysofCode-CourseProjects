## Things learned
# APIs & API Endpoints
# Requests Module
# Response Codes
# API Parameters

import requests
from datetime import datetime

### ISS API Intro
# URL = "http://api.open-notify.org/iss-now.json"

# response = requests.get(url=URL)
# # if response.status_code == 404:
# #     raise Exception("That resource does not exist")
# # if response.status_code == 401:
# #     raise Exception("You are not authorized to access that resource")
# # response.raise_for_status() # Accomplishes the same as manual if loops

# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]

### Sunrise and Sunset Exercise
LAT = 34.052235
LONG = -118.243683

parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)

time_now = datetime.now()
print(time_now.hour)