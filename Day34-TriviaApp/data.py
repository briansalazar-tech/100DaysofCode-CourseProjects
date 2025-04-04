import requests

URL = "https://opentdb.com/api.php"
parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()

# Returns a dictionary of question data used for the quiz
question_data = response.json()["results"]