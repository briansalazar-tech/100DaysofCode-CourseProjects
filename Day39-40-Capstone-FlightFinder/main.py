import os
import time
from notification_manager import NotificationManager
from datetime import datetime, timedelta
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

load_dotenv()

origin_city = os.getenv("ORIGIN_CITY")

spreadsheet_data = DataManager()
flight_search = FlightSearch()
print("Connecting to Google Sheets...")
## Populate the Google Sheet with IATA codes for each city
for entry in range(len(spreadsheet_data.price_data["prices"])):
    if spreadsheet_data.price_data["prices"][entry]["iataCode"] == "":
        city = spreadsheet_data.price_data["prices"][entry]["city"]
        iata_code = flight_search.get_iata_code(city)
        row_id = entry + 2

        spreadsheet_data.set_iata_code(iata_code=iata_code, row_id=row_id)

print("Flight-Deals spreadsheet populated with IATA codes")

## Retreive Google Sheet data
print("Retreiving flight deals data from spreadsheet...")
flight_deals_data = spreadsheet_data.price_data

## Get flight data from API call
month_away = datetime.now() + timedelta(days=30) # Departure date is 30 days from now
futuredate = timedelta(days=7, hours=0, minutes=0) # Return date is 7 days after departure date
one_week_dif = month_away + futuredate

# Formatted dates for API call
dep_date = month_away.strftime("%Y-%m-%d")
ret_date = one_week_dif.strftime("%Y-%m-%d")

flights_results = []

print("Checking for flights to all destinations...")
for entry in flight_deals_data["prices"]:
    flight_data = FlightData()
    city = entry["city"]
    destination_iata = entry["iataCode"]

    print(f"Searching flights to: {city}")
    search_return = flight_search.get_flight_data(destination=destination_iata, departure_date=dep_date, return_date=ret_date)
    parsed_data = flight_data.parse_flight_data(data=search_return)
    if parsed_data[0] == 10000:
        print(f"No direct flights found to {city}. Searching for flights with layovers...")
        modified_search = flight_search.get_flight_data(destination=destination_iata, departure_date=dep_date, return_date=ret_date, is_direct=False)
        parsed_data = flight_data.parse_flight_data(data=modified_search)
    dict_data = {
        "destination": city,
        "lowest_price": round(parsed_data[0], 2),
        "departure_datetime": parsed_data[1],
        "return_datetime": parsed_data[2],
        "average_price": round(parsed_data[3], 2),
        "highest_price": round(parsed_data[4], 2),
        "destination_layovers": parsed_data[5],
        "return_layovers": parsed_data[6]
    }

    flights_results.append(dict_data)
    time.sleep(2)

# Get list of customer emails from Google Sheet
emails = spreadsheet_data.get_customer_emails()

## Compare flight-deals prices with query prices and send email if deal found
print("Comparing flight prices with spreadsheet data to see if deal is found...")
for city in flight_deals_data["prices"]:
    city_name = city["city"]
    for flight in flights_results:

        # Send email if deal found
        if flight["destination"] == city_name and flight["lowest_price"] < city["lowestPrice"]:
            email_manager = NotificationManager(city=city_name)
            body = f"Flight Deal Found!\nFlight to {flight["destination"]} from {origin_city} found for a price of ${flight["lowest_price"]} which is lower than the set threshold of ${city["lowestPrice"]}.\n"
            body += f"Departure Date & Time: {flight["departure_datetime"]}\nReturn Date & Time: {flight["return_datetime"]}\n"
            body += f"Other Query Data:\n\tDeparture & return dates: {dep_date} & {ret_date}\n\tAverage Price: ${flight["average_price"]}\n\tHighest Price: ${flight["highest_price"]}\n"
            body += f"\tLayovers to the destination: {flight["destination_layovers"]}\n\tLayovers on the return: {flight["return_layovers"]}"
            email_manager.send_email(message=body)