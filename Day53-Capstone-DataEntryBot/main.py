import os
import requests
import time
from pprint import pprint
from dotenv import load_dotenv
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

## PART 1 - Scrape Zillow clone website ##
# Get HTML content from the clone Zillow website
response = requests.get(url=ZILLOW_URL)
response.raise_for_status()
response_text = response.text

soup = bs(response_text, "html.parser")

# Property address
address_html = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
property_addresses = []
# Clean up the property address data
for address in address_html:
    address = address.get_text().strip()
    property_addresses.append(address)
print(len(property_addresses))

# Property price
price_html = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
property_prices = []
# Clean up the price data
for card in price_html:
    price = card.get_text()
    price = price.replace("$", "")
    price = price.replace(",", "")
    if "+" in price:
        price = price.split("+")[0]
    if "/" in price:
        price = price.split("/")[0]
    property_prices.append(float(price))
print(len(property_prices))

# Property link
link_html = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
property_links = []
for link in link_html:
    link = link.get("href")
    property_links.append(link)
print(len(property_links))

## PART 2 - Enter data into Google Sheets ##