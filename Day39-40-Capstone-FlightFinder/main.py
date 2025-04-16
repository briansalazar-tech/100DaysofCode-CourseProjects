#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
## Requirements ##
# Message should include the departure airport IATA COde, destination airport IATA code, flight price and flight dates


import requests
import os
import time
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

origin_city = os.getenv("ORIGIN_CITY")

# spreadsheet_data = DataManager()
# flight_search = FlightSearch()


# # Populate the Google Sheet with IATA codes for each city
# for entry in range(len(spreadsheet_data.data["prices"])):
#     if spreadsheet_data.data["prices"][entry]["iataCode"] == "":
#         city = spreadsheet_data.data["prices"][entry]["city"]
#         iata_code = flight_search.get_iata_code(city)
#         row_id = entry + 2

#         spreadsheet_data.set_iata_code(iata_code=iata_code, row_id=row_id)

# print("Flight-Deals spreadsheet populated with IATA codes")

# Retreive Sheetly Data
#flight_deals_data = spreadsheet_data.data
flight_deals_data = {'prices': [
    {'city': 'Los Angeles', 'iataCode': 'LAX', 'lowestPrice': 210, 'id': 2}, 
    {'city': 'Las Vegas', 'iataCode': 'LAS', 'lowestPrice': 100, 'id': 3}, 
    {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 300, 'id': 4}, 
    {'city': 'Chicago', 'iataCode': 'CHI', 'lowestPrice': 551, 'id': 5}, 
    {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 95, 'id': 6}, 
    {'city': 'Boston', 'iataCode': 'BOS', 'lowestPrice': 800, 'id': 7}, 
    {'city': 'San Diego', 'iataCode': 'SAN', 'lowestPrice': 250, 'id': 8}, 
    {'city': 'Miami', 'iataCode': 'MIA', 'lowestPrice': 800, 'id': 9}, 
    {'city': 'Atlanta', 'iataCode': 'ATL', 'lowestPrice': 700, 'id': 10}
    ]}

# Get flight data from API call
month_away = datetime.now() + timedelta(days=30)
futuredate = timedelta(days=7, hours=0, minutes=0)
one_week_dif = month_away + futuredate

dep_date = month_away.strftime("%Y-%m-%d")
ret_date = one_week_dif.strftime("%Y-%m-%d")

# flights_results = []
# for entry in flight_deals_data["prices"]:
#     flight_data = FlightData()
#     city = entry["city"]
#     destination_iata = entry["iataCode"]
#     print(f"Searching flights to: {city}")

#     search_return = flight_search.get_flight_data(destination=destination_iata, departure_date=dep_date, return_date=ret_date)
#     parsed_data = flight_data.parse_flight_data(data=search_return)
    
#     dict_data = {
#         "destination": city,
#         "lowest_price": round(parsed_data[0], 2),
#         "departure_datetime": parsed_data[1],
#         "return_datetime": parsed_data[2],
#         "average_price": round(parsed_data[3], 2),
#         "highest_price": round(parsed_data[4], 2),
#     }

#     flights_results.append(dict_data)
#     time.sleep(2)

# print(flights_results)

test = [{'destination': 'Los Angeles', 'lowest_price': 202.6, 'departure_datetime': '2025-05-16 at 19:38:00', 'return_datetime': '2025-05-23 at 23:32:00', 'average_price': 42.73, 'highest_price': 512.74}, 
        {'destination': 'Las Vegas', 'lowest_price': 107.96, 'departure_datetime': '2025-05-16 at 20:13:00', 'return_datetime': '2025-05-23 at 19:16:00', 'average_price': 23.21, 'highest_price': 116.04}, 
        {'destination': 'San Francisco', 'lowest_price': 278.94, 'departure_datetime': '2025-05-16 at 06:00:00', 'return_datetime': '2025-05-23 at 23:48:00', 'average_price': 16.21, 'highest_price': 388.97}, 
        {'destination': 'Chicago', 'lowest_price': 597.98, 'departure_datetime': '2025-05-16 at 07:05:00', 'return_datetime': '2025-05-23 at 22:27:00', 'average_price': 597.98, 'highest_price': 597.98}, 
        {'destination': 'New York', 'lowest_price': 10000, 'departure_datetime': 'No results found', 'return_datetime': None, 'average_price': 0, 'highest_price': 0}, 
        {'destination': 'Boston', 'lowest_price': 10000, 'departure_datetime': 'No results found', 'return_datetime': None, 'average_price': 0, 'highest_price': 0}, 
        {'destination': 'San Diego', 'lowest_price': 10000, 'departure_datetime': 'No results found', 'return_datetime': None, 'average_price': 0, 'highest_price': 0}, 
        {'destination': 'Miami', 'lowest_price': 10000, 'departure_datetime': 'No results found', 'return_datetime': None, 'average_price': 0, 'highest_price': 0}, 
        {'destination': 'Atlanta', 'lowest_price': 10000, 'departure_datetime': 'No results found', 'return_datetime': None, 'average_price': 0, 'highest_price': 0}
        ]

# Compare flight-deals prices with query prices
for city in flight_deals_data["prices"]:
    city_name = city["city"]
    for flight in test:
        if flight["destination"] == city_name and flight["lowest_price"] < city["lowestPrice"]:
            email_manager = NotificationManager()
            # body = ""
            body = f"Flight Deal Found!\nFlight to {flight["destination"]} from {origin_city} found for a price of ${flight["lowest_price"]} which is lower than the set threshold of ${city["lowestPrice"]}.\n"
            body += f"Departure Date & Time: {flight["departure_datetime"]}\nReturn Date & Time: {flight["return_datetime"]}\n"
            body += f"Other Query Data:\n\tDeparture & return dates: {dep_date} & {ret_date}\n\tAverage Price: ${flight["average_price"]}\n\tHighest Price: ${flight["highest_price"]}"
            # print(body)
            email_manager.send_email(message=body)


# Send email if lowest price lower than data in spreadsheet