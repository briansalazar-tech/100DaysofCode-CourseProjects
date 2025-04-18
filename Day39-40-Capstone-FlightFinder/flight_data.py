class FlightData:
    
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.lowest_price = 10000 # Arbitrary high number to ensure data is returned
        self.date_of_departure = None
        self.date_of_return = None
        self.average_price = 0
        self.sum_of_prices = 0
        self.highest_price = 0
        self.entries = 0
        self.to_stops = 0 # Layovers to destination
        self.return_stops = 0 # Layovers to return


    def parse_flight_data(self, data):
        """
        Takes data from the flight search API and parses the JSON data to find the lowest price, departure date, return date, average price, and highest price.
        Tuple is returned with the data that is found from the JSON data parsed.
        """
        for entry in data["data"]:
            
            # Calculate the average price for the flights returned
            self.sum_of_prices += float(entry["price"]["total"])
            self.entries += 1
            self.average_price = self.sum_of_prices / self.entries
            # Get the highest price
            if float(entry["price"]["total"]) > self.highest_price:
                self.highest_price = float(entry["price"]["total"])
            # Get the lowest price & departure/return times for flight associated with lowest price
            if float(entry["price"]["total"]) < self.lowest_price:
                self.lowest_price = float(entry["price"]["total"])
                self.date_of_departure = entry["itineraries"][0]["segments"][0]["departure"]["at"] # Departure date/time
                self.date_of_return = entry["itineraries"][1]["segments"][0]["arrival"]["at"] # Return date/time
            # Get nummber of stops
            self.to_stops = len(entry["itineraries"][0]["segments"]) - 1
            self.return_stops = len(entry["itineraries"][0]["segments"]) - 1

        # Format the date strings. Some dates may not have flights so departure/return dates will not be returned
        try:
            self.date_of_departure = self.date_of_departure.replace("T", " at ")
            self.date_of_return = self.date_of_return.replace("T", " at ")
        
        except:
            self.date_of_departure = "No results found"
            self.date_of_departure = "No results found"

        return (self.lowest_price, self.date_of_departure, self.date_of_return, self.average_price, self.highest_price, self.to_stops, self.return_stops)
