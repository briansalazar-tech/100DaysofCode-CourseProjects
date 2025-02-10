print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n"))
tip_choice = float(input("What percentage tip would you like to give? 10%, 12%, or 15%?\n"))
people = int(input("How many people to split the bill?\n"))

tip = tip_choice / 100 # Convert tip percentage to decimal
total_bill = bill + (bill * tip) # Calculate total bill with tip included
bill_per_person = round(total_bill / people, 2) # Total to pay per person

print(f"The total bill with tip included is ${total_bill}. Each person should pay: ${bill_per_person}")