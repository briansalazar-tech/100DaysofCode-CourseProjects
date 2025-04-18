import os
import requests
from dotenv import load_dotenv

load_dotenv()


class DataManager:

    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.price_data = {} # Price data from the Google Sheet
        self.user_data = {} # User data from Google Sheet
        self.sheetly_price_endpoint = os.getenv("SHEETLY_FLIGHTDEALS_PRICES_ENDPOINT")
        self.sheetly_user_endpoint = os.getenv("SHEETLY_FLIGHTSDEALS_USERS_ENDPOINT")
        self.sheetly_auth = os.getenv("SHEETLY_FLIGHTDEALS_AUTHENTICATION")
        self.sheetly_headers = {
            "Authorization": self.sheetly_auth,
        }
        
        self.get_data()


    def get_data(self):
        """Populates the data attribute with the data from the Google Sheet."""
        price_response = requests.get(url=self.sheetly_price_endpoint, headers=self.sheetly_headers)
        price_response.raise_for_status()
        self.price_data = price_response.json()

        user_response = requests.get(url=self.sheetly_user_endpoint, headers=self.sheetly_headers)
        user_response.raise_for_status()
        self.user_data = user_response.json()


    def get_customer_emails(self):
        """Returns a list of customer emails from the Google Sheet"""
        emails = []
        for user in self.user_data["users"]:
            emails.append(user["enterYourEmail"])
        return emails


    def set_iata_code(self, iata_code, row_id):
        """Sets IATA code in the GOogle Sheet for the given row ID. Data attribute is updated with the new data."""
        endpoint = f"{self.sheetly_price_endpoint}/{row_id}"
        updated_data = {
            "price": {
                "iataCode": iata_code
            }
        }

        response = requests.put(
            url=endpoint,
            headers=self.sheetly_headers,
            json=updated_data,
        )
        response.raise_for_status()
        self.get_data()
        
        print("IATA code updated to: " + iata_code)
