import requests
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.getenv("ALPHAVANTAGE_KEY")
NEWS_API_KEY = os.getenv("NEWSAPI_KEY")
yesterday_date = "2025-04-04"
day_before_yesterday_date = "2025-04-03"

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

# stocks_response = requests.get(STOCK_URL, params=alphavantage_parameters)
# stocks_response.raise_for_status()
# stocks_data = stocks_response.json()
# stocks_data_filtered = stocks_data["Time Series (Daily)"]

# # STEP 1: Get stock closing prices for yesterday and the day before
# # Get yesterday's and day before yesterday's closing prices. Loop ensures that weekend days are not included

# yesterday_close = ""
# day_before_yesterday_close = ""
# count = 0
# for key, value in stocks_data_filtered.items():
#     if count != 3:
#         if count > 0 and count < 3:
#             if count == 1:
#                 yesterday_date = key
#                 yesterday_close = float(value["4. close"])
#             if count == 2:
#                 day_before_yesterday_date = key
#                 day_before_yesterday_close = float(value["4. close"])       
#         count += 1

# TESTING


yesterday_close = 239.4300

day_before_yesterday_close = 267.2800

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
difference = round((yesterday_close - day_before_yesterday_close) / ((yesterday_close + day_before_yesterday_close) / 2) * 100, 2)
# print(abs(difference))

if abs(difference) >= 5:
    pass


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# news_response = requests.get(NEWS_URL, params=news_parameters)
# news_response.raise_for_status()
# news_data = news_response.json()["articles"][0:3]

news_data = [{'source': {'id': None, 'name': 'Yahoo Entertainment'}, 'author': 'Soma Dutta', 'title': 'Tesla, Inc. (TSLA): The Best Climate Change Stock to Buy Now', 'description': 'We recently published a list of 10 Best Climate Change Stocks to Buy Now. In this article, we will look at where Tesla, Inc. (NASDAQ:TSLA) stands against...', 'url': 'https://finance.yahoo.com/news/tesla-inc-tsla-best-climate-105621860.html', 'urlToImage': 'https://s.yimg.com/ny/api/res/1.2/R3DsTXHuX1Up50du0B.awA--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyMDA7aD02NzM-/https://media.zenfs.com/en/insidermonkey.com/1277c6032fd09b727a10249a170024cf', 'publishedAt': '2025-04-03T10:56:21Z', 'content': 'We recently published a list of\xa010 Best Climate Change Stocks to Buy Now. In this article, we will look at where Tesla, Inc. (NASDAQ:TSLA) stands against other best climate change stocks to buy now.\r… [+6757 chars]'}, {'source': {'id': None, 'name': 'Quartz India'}, 'author': 'Kevin Williams', 'title': 'These stocks mostly dodged the tariffs plunge — for now', 'description': 'While much of the attention was focused on the beating taken by stocks Thursday, a few that escaped unscathed. After all, tariffs have an unequal effect, hitting some businesses harder than others.Read more...', 'url': 'https://qz.com/stocks-that-did-well-thursday-despite-tariffs-1851774672', 'urlToImage': 'https://i.kinja-img.com/image/upload/c_fill,h_675,pg_1,q_80,w_1200/95b4eeb3c6489c028f88389b173a1312.jpg', 'publishedAt': '2025-04-03T20:54:00Z', 'content': 'In This Story\r\nWhile much of the attention was focused on the beating taken by stocks Thursday, a few that escaped unscathed. After all, tariffs have an unequal effect, hitting some businesses harder… [+2376 chars]'}, {'source': {'id': None, 'name': 'Forbes'}, 'author': 'Danielle Chemtob, Forbes Staff, \n Danielle Chemtob, Forbes Staff\n https://www.forbes.com/sites/daniellechemtob/', 'title': 'Forbes Daily: Tariff ‘Liberation Day’ Sinks Stocks As China Retaliates', 'description': 'Today’s Forbes Daily newsletter covers Wall Street souring on Trump, the biggest billionaire tariff losers, DOGE cuts worsen March layoffs and more.', 'url': 'https://www.forbes.com/sites/daniellechemtob/2025/04/04/forbes-daily-tariff-liberation-day-sinks-stocks-as-china-retaliates/', 'urlToImage': 'https://imageio.forbes.com/specials-images/imageserve/67efceea3a88c3ca552dbe78/0x0.jpg?format=jpg&crop=2120,1192,x0,y109,safe&height=900&width=1600&fit=bounds', 'publishedAt': '2025-04-04T12:28:11Z', 'content': 'President Donald Trumps tariff Liberation Day turned into a Wall Street bloodbath.\r\nThe tariffs on nearly all foreign nations are widely expected to raise prices for American consumers. And despite t… [+7167 chars]'}]

email_body = f"{STOCK} news:\n"
for entry in news_data:
    title = entry["title"]
    description = entry["description"]
    url = entry["url"]
    email_body += f"Headline: {title}\nBrief: {description}\nLink to article: {url}\n\n"

print(email_body)
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

