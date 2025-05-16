import os
import requests
import time
from dotenv import load_dotenv
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORMS_URL = os.getenv("PROPERTY_FORMS_URL")
CHROME_OPTIONS = webdriver.ChromeOptions().add_experimental_option("detach", True)

driver = webdriver.Chrome(options=CHROME_OPTIONS)

## PART 1 - Scrape Zillow clone website ##
print("Opening Zillow clone website and scraping necessary data...")
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

# Property link
link_html = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
property_links = []
for link in link_html:
    link = link.get("href")
    property_links.append(link)

# Create list for dictionary data
properties = []
# Create dictionary of property data
for index in range(len(property_addresses)):
    property_data = {
        "address": property_addresses[index],
        "price": property_prices[index],
        "link": property_links[index],
    }
    properties.append(property_data)

print("Properties dicitonary created")

## PART 2 - Enter data into Google Sheets ##
print("Opening Google Forms...")
fill_form = driver.get(url=FORMS_URL)
# Enter forms data using for loop
for index in range(len(properties)):
    address = properties[index]["address"]
    price = properties[index]["price"]
    link = properties[index]["link"]
    
    print(f"Adding the following address to Forms response: {address}")
    
    # Enter address
    address_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(address)
    time.sleep(2)
    # Enter price
    price_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.send_keys(price)
    time.sleep(2)
    # Enter link
    link_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.send_keys(link)
    time.sleep(2)
    # Click submit button
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_button.click()
    time.sleep(3)
    # Click submit another response link
    submit_another_link = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another_link.click()

    time.sleep(3)

# Close browser
driver.quit()
print("All data has been entered into the Google forms. Exiting program...")