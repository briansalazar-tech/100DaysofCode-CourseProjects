import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = os.getenv("PIXELA_TOKEN")
USERNAME = os.getenv("PIXELA_USER")
GRAPH_ID = "graph1"

# PIXEL DATA. Change values and uncomment desired activity to perform
date = datetime(year=2025, month=4, day=3) # Enter the date you want to log data for
formatted_date =date.strftime("%Y%m%d")
quantity = 1.0 # Enter the quantity to log

headers = {
    "X-USER-TOKEN": TOKEN
}

## Step 1: User creation - Once account is created, lines can be commented out.
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
# print(response.text)

## Step 2: Create a graph ##
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_configuration = {
    "id": "graph1",
    "name": "Running Milage",
    "unit": "Mi",
    "type": "float",
    "color": "sora",
}

# response = requests.post(url=graph_endpoint, json=graph_configuration, headers=headers)
# print(response.text)

## Step 3: Log pixel data ##
pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": formatted_date, # YYYMMDD format
    "quantity": str(quantity),
}

response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)

## Step 4: Update pixel data ##
pixel_update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"

update_data = {
    "quantity": str(quantity),
}

# response = requests.put(url=pixel_update_endpoint, json=update_data, headers=headers)
# print(response.text)

## Step 5: Delete pixel data ##
pixel_delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)