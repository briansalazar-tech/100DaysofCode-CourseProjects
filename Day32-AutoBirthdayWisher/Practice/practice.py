import smtplib
import datetime as dt
import random

with open(file="./Day32-AutoBirthdayWisher/quotes.txt", mode="r") as quotes:
    quote_list = quotes.readlines()
random_quote = random.choice(quote_list)


now = dt.datetime.now()
# year = now.year
# month = now.month
day_of_week = now.weekday()
# if year == 2025:
#     print("The year is current")
# print(day_of_week)

# date_of_birth = dt.datetime(year=1994, month=12, day=1)
# print(day_of_week)

my_email = "email@email"
to_address = "email@email"
password = "apppassword"

# Method 1 for sending emails
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, 
#                     to_addrs=to_address, 
#                     msg="Subject:Hello\n\nThis is the body of my email.")
# connection.close()

if day_of_week == 1:
# Method 2 for sending emails
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs=to_address, 
                            msg=f"Subject:Monday Motivation\n\n{random_quote}"
                            )
        print("Email sent")
