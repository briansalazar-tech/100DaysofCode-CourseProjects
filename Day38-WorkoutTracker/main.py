import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# Nutritionix API parameters
GENDER = "male"
AGE = 30
WEIGHT_KG = 55
HEIGHT_CM = 67.64

NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIXAPP_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIXAPI_KEY")
NUTRITIONIX_EXERCISE_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETLY_ENDPOINT = os.getenv("SHEETLY_ENDPOINT")

## 1. Use user input to get exercise data from the Nutritionix API
user_input = input("What exercise did you do today? ") # Ex. I ran 1 mile

nutritionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

nutritionix_parameters = {
    "query": user_input, # Change to input from user
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=NUTRITIONIX_EXERCISE_ENDPOINT, json=nutritionix_parameters, headers=nutritionix_headers)
response.raise_for_status()
exercise_data = response.json()

##  2. Transform exercise data for the workout-tracker spreadsheet
date = datetime.today().strftime("%m/%d/%Y") # MM/DD/YYYY
time = datetime.today().strftime("%X") # HH:MM:SS
exercise = exercise_data["exercises"][0]["user_input"].title()
duration = exercise_data["exercises"][0]["duration_min"]
calories = exercise_data["exercises"][0]["nf_calories"]

## 3. Upload data to Google Sheets using Sheetly API
sheetly_headers = {
    "Authorization": os.getenv("SHEETLY_AUTHENTICATION")
}

sheetly_data = {
    "sheet1": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}

# Add data to the workout-tracker spreadsheet
response = requests.post(url=SHEETLY_ENDPOINT, json=sheetly_data, headers=sheetly_headers)
response.raise_for_status()
print(f"New row of data added:\n{response.json()}")