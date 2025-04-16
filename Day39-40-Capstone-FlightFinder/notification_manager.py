import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:

    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.email = os.getenv("TEST_EMAIL")
        self.password = os.getenv("TEST_EMAIL_APP_PW")
        self.to_address = os.getenv("TEST_EMAIL")
        self.subject = "Low Price Alert!! Flight Deal Found! ✈️"


    def send_email(self, message):
        """Takes a formatted message and sends an email to the to_address specified in the envirnemnt variable."""
        print("Deal found. Sending email...")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(from_addr=self.email,
                                to_addrs=self.to_address,
                                msg=f"Subject:{self.subject}\n\n{message}".encode("utf-8")
                                )
        print("Email Sent!")