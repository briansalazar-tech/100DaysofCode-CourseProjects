#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
## Requirements ##
# Use Flight Search API to check the cheapest flight from tomorrow to 6 months later for all cities in google sheet
# If price is lower than lowest price in googlee sheet, send email using SMTPlib
# Message should include the departure airport IATA COde, destination airport IATA code, flight price and flight dates


import requests
import os
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

spreadsheet_data = DataManager()
flight_search = FlightSearch()

# Populate the Google Sheet with IATA codes for each city
for entry in range(len(spreadsheet_data.data["prices"])):
    if spreadsheet_data.data["prices"][entry]["iataCode"] == "":
        city = spreadsheet_data.data["prices"][entry]["city"]
        iata_code = flight_search.get_iata_code(city)
        row_id = entry + 2

        spreadsheet_data.set_iata_code(iata_code=iata_code, row_id=row_id)

print("Flight-Deals spreadsheet populated with IATA codes")