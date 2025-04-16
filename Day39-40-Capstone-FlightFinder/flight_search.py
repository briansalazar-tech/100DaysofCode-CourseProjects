import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN_ENDPOINT = os.getenv("AMADEUS_TOKEN_ENDPOINT")
FLIGHT_SEARCH_ENDPOINT = os.getenv("AMADEUS_SEARCH_ENDPOINT")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):

        self._api_key = os.getenv("AMADEUS_KEY")
        self._api_secret = os.getenv("AMADEUS_SECRET")
        self._token = self._get_new_token()


    def _get_new_token(self):
        """Calls the Amadeus Toekn endpoint to retreive a new access token. Once token generated and saved, method not needed."""
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret,
        }

        response = requests.post(url=TOKEN_ENDPOINT, 
                                 headers=header, 
                                 data=body)
        response.raise_for_status()
        token = response.json()["access_token"]
        print(f"Generated Token is: {token}")
        return token

    def get_iata_code(self, city_name):
        header = {
            "Authorization": f"Bearer {self._token}",
        }

        parameters = {
            "countryCode": "US",
            "keyword": city_name,
            "max": 1,
        }

        response = requests.get(url="https://test.api.amadeus.com/v1/reference-data/locations/cities", headers=header, params=parameters)
        response.raise_for_status()
        response_json = response.json()
        iatacode = response_json["data"][0]["iataCode"]
        return iatacode
    

    def get_flight_data(self, destination, departure_date, return_date):
        header = {
            "Authorization": f"Bearer {self._token}",
        }

        body = {
            "originLocationCode": os.getenv("ORIGIN_IATA"),
            "destinationLocationCode": destination,
            "departureDate": departure_date,
            "returnDate": return_date,
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "USD",
            "max": 50,
        }

        response = requests.get(
            url=FLIGHT_SEARCH_ENDPOINT,
            headers=header,
            params=body,
        )
        response.raise_for_status()
        flight_data = response.json()

        # print(flight_data)
        return flight_data