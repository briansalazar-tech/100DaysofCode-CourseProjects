import os
import requests
from dotenv import load_dotenv

load_dotenv()


class DataManager:

    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = {} # Data from the Google Sheet
        self.sheetly_endpoint = os.getenv("SHEETLY_FLIGHTDEALS_ENDPOINT")
        self.sheetly_auth = os.getenv("SHEETLY_FLIGHTDEALS_AUTHENTICATION")
        self.sheetly_headers = {
            "Authorization": self.sheetly_auth,
        }
        
        self.get_data()


    def get_data(self):
        """Populates the data attribute with the data from the Google Sheet."""
        response = requests.get(url=self.sheetly_endpoint, headers=self.sheetly_headers)
        response.raise_for_status()
        self.data = response.json()


    def set_iata_code(self, iata_code, row_id):
        """Sets IATA code in the GOogle Sheet for the given row ID. Data attribute is updated with the new data."""
        endpoint = f"{self.sheetly_endpoint}/{row_id}"
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
