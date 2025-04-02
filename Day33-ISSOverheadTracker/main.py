import os
import smtplib
import requests
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
EMAIL = os.getenv("TEST_EMAIL")
PASSWORD = os.getenv("TEST_EMAIL_APP_PW")


def check_if_overhead():
    """Checks to see if the ISS is overhead within a lat/long of 5"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check if current position is +/-5 within ISS current position
    abs_lat = abs(iss_latitude - MY_LAT)
    abs_long = abs(iss_longitude - MY_LONG)
    
    if abs_lat <= 5 and abs_long <= 5:
        return True
    
    return False


def check_if_night():
    """Get sunrise and sunset hours and check if current time falls before sunrise or after sunset"""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour

    if hour < sunrise or hour > sunset:
        return True
    
    return False


# Run code every 60 seconds to check if ISS is overhead and it is dark outside
while True:
    is_overhead = check_if_overhead()
    is_nighttime = check_if_night()
    time.sleep(60)
    if is_overhead and is_nighttime:
        print("ISS overhead")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(
                user=EMAIL,
                password=PASSWORD
            )
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg="Subject:ISS is Overhead\n\nLook up!\nISS is overhead and it is dark outside!"
            )
            print("Email sent successfully")
