import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Get cookie button
cookie = driver.find_element(By.ID, value="cookie")

# Get upgrade items
items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_id = []
for item in items:
    item_id.append(item.get_attribute("id"))

# Check item prices every 5 seconds
check_price = time.time() + 5
game_end = time.time() + 60 * 5 # 5 minutes

while True:
    cookie.click()
    store_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
    item_prices = []

    if time.time() > check_price:

        # Get the price from the CSS selector
        for item in store_prices:
            if item.text != "":
                cost = int(item.text.split("-")[1].replace(",", "").strip())
                item_prices.append(cost)

        # Create dictionary of items and their prices
        store_upgrades = {}
        for item in range(len(item_prices)):
            store_upgrades[item_prices[item]] = item_id[item]
        
        # Get money count
        money = int(driver.find_element(By.ID, value="money").text.replace(",", ""))

        # Items that can be bought
        affordable_items = {}
        for cost, id in store_upgrades.items():
            if money > cost:
                affordable_items[cost] = id

        # Purchase upgrade
        try:
            highest_priced_item = max(affordable_items)
            print(f"highest_affordable: {highest_priced_item}")
            item_to_purchase_id = affordable_items[highest_priced_item]
            driver.find_element(By.ID, value=item_to_purchase_id).click()
        except ValueError:
            print("No items avaialble for purchase")
            pass

    # Break loop after 5 minutes
    if time.time() > game_end:
        cookies_per_second = driver.find_element(By.ID, value="cps").text
        print(f"Cookies per second after 5 minutes: {cookies_per_second}")
        break