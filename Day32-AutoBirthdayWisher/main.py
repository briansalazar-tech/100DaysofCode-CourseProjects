import os
import pandas
import smtplib
import datetime as dt
from random import choice
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

email = os.getenv("TEST_EMAIL")
password = os.getenv("TEST_EMAIL_APP_PW")

person_name = ""
to_address = ""
now = dt.datetime.now()
day = now.day
month = now.month

# Load Letter temilates
letter_templates = []
with open(file="./Day32-AutoBirthdayWisher/letter_templates/letter_1.txt", mode="r") as letter1:
    template_1 = letter1.read()
    letter_templates.append(template_1)
with open(file="./Day32-AutoBirthdayWisher/letter_templates/letter_2.txt", mode="r") as letter2:
    template_2 = letter2.read()
    letter_templates.append(template_2)
with open(file="./Day32-AutoBirthdayWisher/letter_templates/letter_3.txt", mode="r") as letter3:
    template_3 = letter3.read()
    letter_templates.append(template_3)

# Check if person has birthday today
birthdays_df = pandas.read_csv("./Day32-AutoBirthdayWisher/birthdays.csv")
birthdays_dict = birthdays_df.to_dict(orient="records")
for record in birthdays_dict:
    if record["month"] == month and record["day"] == day:
        person_name = record["name"]
        to_address = record["email"]

# Compose email
template = choice(letter_templates)
subject= "Happy Birthday!!"
email_body = template.replace("[NAME]", person_name)

# Send email
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email,
                        to_addrs=to_address,
                        msg=f"Subject:{subject}\n\n{email_body}"
                        )
    print("Email sent sucessfully")