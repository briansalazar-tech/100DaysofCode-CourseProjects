import requests
import os
from dotenv import load_dotenv

load_dotenv()

NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIXAPP_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIXAPI_KEY")
NUTRITIONIX_EXERCISE_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

nutritionix_parameters = {
    "query": "I ran 1 mile", # Change to input from user
    "gender": "male", # Constant
    "weight_kg": 55, # Constant
    "height_cm": 167.64, # Constant
    "age": 30, # Constant
}

response = requests.post(url=NUTRITIONIX_EXERCISE_ENDPOINT, json=nutritionix_parameters, headers=nutritionix_headers)
response.raise_for_status()
exercise_data = response.json()
print(exercise_data)