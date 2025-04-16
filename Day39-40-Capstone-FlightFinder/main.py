#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
## Requirements ##
# Use Flight Search API to check the cheapest flight from tomorrow to 6 months later for all cities in google sheet
# If price is lower than lowest price in googlee sheet, send email using SMTPlib
# Message should include the departure airport IATA COde, destination airport IATA code, flight price and flight dates


import requests
import os
import time
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from pprint import pprint
from datetime import datetime, timedelta
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

# Retreive Sheetly Data
flight_deals_data = spreadsheet_data.data
flight_deals_data = {'prices': [{'city': 'Los Angeles', 'iataCode': 'LAX', 'lowestPrice': 54, 'id': 2}, {'city': 'Las Vegas', 'iataCode': 'LAS', 'lowestPrice': 42, 'id': 3}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 485, 'id': 4}, {'city': 'Chicago', 'iataCode': 'CHI', 'lowestPrice': 551, 'id': 5}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 95, 'id': 6}, {'city': 'Boston', 'iataCode': 'BOS', 'lowestPrice': 414, 'id': 7}, {'city': 'San Diego', 'iataCode': 'SAN', 'lowestPrice': 240, 'id': 8}, {'city': 'Miami', 'iataCode': 'MIA', 'lowestPrice': 260, 'id': 9}, {'city': 'Atlanta', 'iataCode': 'ATL', 'lowestPrice': 378, 'id': 10}]}

# Get flight data from API call
month_away = datetime.now() + timedelta(days=30)
futuredate = timedelta(days=7, hours=0, minutes=0)
one_week_dif = month_away + futuredate

dep_date = month_away.strftime("%Y-%m-%d")
ret_date = one_week_dif.strftime("%Y-%m-%d")

flights_results = []
for entry in flight_deals_data["prices"]:
    flight_data = FlightData()
    city = entry["city"]
    destination_iata = entry["iataCode"]
    print(f"Searching flights to: {city}")

    search_return = flight_search.get_flight_data(destination=destination_iata, departure_date=dep_date, return_date=ret_date)
    parsed_data = flight_data.parse_flight_data(data=search_return)
    
    dict_data = {
        "destination": city,
        "lowest_price": round(parsed_data[0], 2),
        "departure_datetime": parsed_data[1],
        "return_datetime": parsed_data[2],
        "average_price": round(parsed_data[3], 2),
        "highest_price": round(parsed_data[4], 2),
    }

    flights_results.append(dict_data)
    time.sleep(2)

print(flights_results)

test = []
# pprint(test)