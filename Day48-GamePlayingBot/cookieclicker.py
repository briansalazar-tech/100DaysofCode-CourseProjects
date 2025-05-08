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
#     money = int(driver.find_element(By.ID, value="money").text)
#     # Buy cursor
#     cursor_price = driver.find_element(By.CSS_SELECTOR, value="#buyCursor b").text
#     cursor_price_int = int(cursor_price.split(" - ")[1].strip())
#     # Buy grandma
#     grandma_price = driver.find_element(By.CSS_SELECTOR, value="#buyGrandma b").text
#     grandma_price_int = int(grandma_price.split(" - ")[1].strip())
    
#     if time.time() > check_price:
#         if money > grandma_price_int:
#             buy_grandma = driver.find_element(By.ID, value="buyGrandma")
#             buy_grandma.click()

#         if money > cursor_price_int:
#             buy_cursur = driver.find_element(By.ID, value="buyCursor")
#             buy_cursur.click()

#         check_price = time.time() + 5

    # Break loop after 5 minutes
    if time.time() > game_end:
        cookies_per_second = driver.find_element(By.ID, value="cps").text
        print(f"Cookies per second after 5 minutes: {cookies_per_second}")
        break