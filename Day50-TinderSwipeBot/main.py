import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

FB_USERNAME = os.getenv("FB_USERNAME")
FB_PASSWORD = os.getenv("FB_PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Open the Tinder website
driver.get(url="https://www.tinder.com")
time.sleep(3)

cookies = driver.find_element(By.XPATH, value='//*[@id="q-637390230"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
cookies.click()
time.sleep(2)

# Login with Facebook
log_in_button = driver.find_element(By.LINK_TEXT, value="Log in")
log_in_button.click()
time.sleep(5)

fb_login = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
fb_login.click()
time.sleep(5)
print("Opening pop up window")
main_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
username = driver.find_element(By.NAME, value="email")
username.send_keys(FB_USERNAME)
time.sleep(5)
password = driver.find_element(By.NAME, value="pass")
password.send_keys(FB_PASSWORD, Keys.ENTER)
driver.switch_to.window(main_window)

# Dismiss pop up windows
time.sleep(10)
allow_location = driver.find_element(By.XPATH, value='//*[@id="q1929195990"]/main/div/div/div/div[3]/button[1]')
allow_location.click()
time.sleep(5)
enable_notifications = driver.find_element(By.XPATH, value='//*[@id="q1929195990"]/main/div/div/div/div[3]/button[2]')
enable_notifications.click()

# Swipe away
for n in range(20):
    time.sleep(5)
    dislike_button = driver.find_element(By.XPATH, value='//*[@id="q-637390230"]/div/div[1]/div/main/div[2]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button')
    dislike_button.click()