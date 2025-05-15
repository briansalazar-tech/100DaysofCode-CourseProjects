import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

load_dotenv()

SEARCH_ACCOUNT = "account_name" # Replace with the account you want to search for
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
CHROME_OPTIONS = webdriver.ChromeOptions().add_experimental_option("detach", True)


class InstagramBot:

    def __init__(self):
        self.driver = webdriver.Chrome(options=CHROME_OPTIONS)

    def login(self):
        instagram = self.driver
        instagram.get(url="https://www.instagram.com/")
        time.sleep(5)

        ig_username = self.driver.find_element(By.NAME, value="username")
        ig_username.send_keys(INSTAGRAM_USERNAME)
        time.sleep(5)

        ig_password = self.driver.find_element(By.NAME, value="password")
        ig_password.send_keys(INSTAGRAM_PASSWORD , Keys.ENTER)
        time.sleep(10)
    
    def follow(self, user_account):
            user_account = self.driver.find_element(By.NAME, value="._acan _acap _acas _aj1-")
            user_account.click()
            time.sleep(5)

    def find_followers(self):
        dont_save = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
        dont_save.click()
        time.sleep(5)

        dont_notify = self.driver.find_element(By.XPATH, value='/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        dont_notify.click()
        time.sleep(5)

        search_button = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a')
        search_button.click()
        time.sleep(5)

        search_bar = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
        search_bar.send_keys(SEARCH_ACCOUNT)
        time.sleep(5)

        select_account = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]')
        select_account.click()
        time.sleep(5)

        following_link = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a')
        following_link.click()
        time.sleep(5)
        print("Getting accounts")
        get_followers = self.driver.find_elements(By.CSS_SELECTOR, ".x1dm5mii")
        print(len(get_followers))
        followers_list = []
        print("Adding accounts to list")
        for account in get_followers:
            followers_list.append(account)
        print(followers_list)
        time.sleep(5)
        print("Itterating through followers....")
        for account in get_followers:
            self.follow(account)
        print("Finished!")


instagram_bot = InstagramBot()
instagram_bot.login()
instagram_bot.find_followers()