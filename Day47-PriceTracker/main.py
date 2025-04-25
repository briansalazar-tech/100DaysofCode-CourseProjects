import os
import requests
import smtplib
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv

load_dotenv()

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
    "Accept-Language": "en-US,en;q=0.9",
}
# URL = "https://appbrewery.github.io/instant_pot/" # Static website
URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1" # Live Site
PRICE_THRESHOLD = 100
EMAIL = os.getenv("TEST_EMAIL")
PASSWORD = os.getenv("TEST_EMAIL_APP_PW")

response = requests.get(url=URL, headers=HEADERS).text
soup = bs(response, "html.parser")
# print(soup.prettify()) # Verify that you are not getting a CAPTCHA page

# Solution uses the find method instead of select
# price = soup.find(class_="a-offscreen").get_text()

# Obtain an items price & name
item_name = soup.find(id="productTitle").get_text().strip().split("\r\n")[0]
price = soup.select_one(selector=".aok-offscreen").getText()
price_float = float(price.split("$")[1])
print(item_name)
print(price_float)

# Email alert when the price is below a preset value
if price_float < PRICE_THRESHOLD:
    print("Price threshold met. Sending email...")
    subject = "Deal on Watchlist Item 💸"
    email_body = f"{item_name} is currently on sale! The current price for the item is ${price_float} which is less than the ${PRICE_THRESHOLD} threshold set!\nHere is the link to your saved item: {URL}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:{subject}\n\n{email_body}".encode("utf-8")
        )

    print("Email sent successfully!")