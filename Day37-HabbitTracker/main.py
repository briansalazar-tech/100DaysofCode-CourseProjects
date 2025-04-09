import requests
import os
from dotenv import load_dotenv

load_dotenv()

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = os.getenv("PIXELA_TOKEN")
USERNAME = os.getenv("PIXELA_USER")

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Step 1: User creation - Once account is created, lines can be commented out.
# response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
# print(response.text)

# Step 2: Create a graph
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_configuration = {
    "id": "graph1",
    "name": "Running Milage",
    "unit": "Mi",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_configuration, headers=headers)
print(response.text)