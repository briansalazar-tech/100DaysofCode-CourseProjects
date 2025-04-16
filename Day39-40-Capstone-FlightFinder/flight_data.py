class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.lowest_price = 10000 # Arbitrary high number to ensure data is returned
        self.date_of_departure = None
        self.date_of_return = None
        self.average_price = 0
        self.highest_price = 0
        self.entries = 0

    def parse_flight_data(self, data):
        for entry in data["data"]:

            sum_of_prices = 0
            sum_of_prices += float(entry["price"]["total"])
            self.entries += 1
            
            self.average_price = sum_of_prices / self.entries

            if float(entry["price"]["total"]) > self.highest_price:
                self.highest_price = float(entry["price"]["total"])

            if float(entry["price"]["total"]) < self.lowest_price:
                self.lowest_price = float(entry["price"]["total"])
                self.date_of_departure = entry["itineraries"][0]["segments"][0]["departure"]["at"]
                self.date_of_return = entry["itineraries"][1]["segments"][0]["arrival"]["at"]
        
        # Format the date strings
        try:
            self.date_of_departure = self.date_of_departure.replace("T", " at ")
            self.date_of_departure = self.date_of_return.replace("T", " at ")
        except:
            self.date_of_departure = "No results found"
            self.date_of_departure = "No results found"

        return (self.lowest_price, self.date_of_departure, self.date_of_return, self.average_price, self.highest_price)
