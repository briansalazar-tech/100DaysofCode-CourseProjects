import requests
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_URL = "https://www.alphavantage.co/query"
NEWS_URL = ""
STOCK_API_KEY = os.getenv("ALPHAVANTAGE_KEY")
NEWS_API_KEY = os.getenv("NEWSAPI_KEY")

alphavantage_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY,
}

news_parameters = {
    "apikey": NEWS_API_KEY
}

# stocks_response = requests.get(STOCK_URL, params=alphavantage_parameters)
# stocks_response.raise_for_status()
# stocks_data = stocks_response.json()
# stocks_data_filtered = stocks_data["Time Series (Daily)"]

## STEP 1: Get stock closing prices for yesterday and the day before
# # Get yesterday's and day before yesterday's closing prices. Loop ensures that weekend days are not included
# yesterday_close = ""
# day_before_yesterday_close = ""
# count = 0
# for key, value in stocks_data_filtered.items():
#     if count != 3:
#         if count > 0 and count < 3:
#             if count == 1:
#                 yesterday_close = float(value["4. close"])
#             if count == 2:
#                 day_before_yesterday_close = float(value["4. close"])       
#         count += 1

# TESTING
yesterday_close = 239.4300
day_before_yesterday_close = 267.2800


# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
difference = round((yesterday_close - day_before_yesterday_close) / ((yesterday_close + day_before_yesterday_close) / 2) * 100, 2)
print(abs(difference))

if abs(difference) >= 5:
    print("Get News")
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

