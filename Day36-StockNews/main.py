import requests
import os
import smtplib
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.getenv("ALPHAVANTAGE_KEY")
NEWS_API_KEY = os.getenv("NEWSAPI_KEY")
email = os.getenv("TEST_EMAIL")
password = os.getenv("TEST_EMAIL_APP_PW")
today = datetime.today().date()

yesterday_date = ""
day_before_yesterday_date = ""

alphavantage_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY,
}

news_parameters = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "from": day_before_yesterday_date,
    "to": yesterday_date,
    "language": "en",
    "sortBy": "relevancy"
}

# Get stock data
stocks_response = requests.get(STOCK_URL, params=alphavantage_parameters)
stocks_response.raise_for_status()
stocks_data = stocks_response.json()
stocks_data_filtered = stocks_data["Time Series (Daily)"]

# STEP 1: Get stock closing prices for yesterday and the day before
# Get yesterday's and day before yesterday's closing prices based on first entries 3 in returned JSON data
# Loop addresses potential for dates falling on weenends
yesterday_close = ""
day_before_yesterday_close = ""
count = 0
for key, value in stocks_data_filtered.items():
    if count != 3:
        if count > 0 and count < 3:
            if count == 1:
                yesterday_date = key
                yesterday_close = float(value["4. close"])
            if count == 2:
                day_before_yesterday_date = key
                day_before_yesterday_close = float(value["4. close"])       
        count += 1

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday compose and send email.
difference = round((yesterday_close - day_before_yesterday_close) / ((yesterday_close + day_before_yesterday_close) / 2) * 100, 2)
if abs(difference) >= 5:

    ## STEP 2: Get news on the company & Format email content
    # Get news articles
    news_response = requests.get(NEWS_URL, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"][0:3]

    # Format email subject and body lines
    gain_or_loss = ""
    if difference > 0:
        gain_or_loss = "🔺"
    else:
        gain_or_loss = "🔻"

    subject = f"STOCK UPDATE {today} - {STOCK}: {gain_or_loss}{abs(difference)}%"
    email_body = f"{STOCK} news:\n"
    for entry in news_data:
        title = entry["title"]
        description = entry["description"]
        url = entry["url"]
        email_body += f"Headline: {title}\nBrief: {description}\nLink to article: {url}\n\n"

    ## STEP 3: Use SMTPLIB to send an email
    print("Sending email...")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=email,
                            msg=f"Subject:{subject}\n\n{email_body}".encode("utf-8"))
        print("Email sent!")
else:
    print("No news to report.")