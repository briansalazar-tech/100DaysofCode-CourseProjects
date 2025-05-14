import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = ""
TWITTER_USERNAME = ""
TWITTER_PASSWORD = None

CHROME_OPTIONS = webdriver.ChromeOptions().add_experimental_option("detach", True)

class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(options=CHROME_OPTIONS)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        start = self.driver
        
        # Start test
        start.get(url="https://www.speedtest.net/")
        time.sleep(5)
        start_button = start.find_element(By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start_button.click()
        time.sleep(75)
        
        # Close pop up
        start_button.send_keys(Keys.ESCAPE)
        time.sleep(5)
        
        # Get Upload & Download Speeds
        upload_speed = start.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = upload_speed
        print(f"Upload speed: {self.up}")
        download_speed = start.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = download_speed
        print(f"Download speed: {self.down}")
        time.sleep(120)
        self.driver.close()

    def tweet_at_provider(self):
        twitter = self.driver
        twitter.get(url="https://twitter.com/?lang=en")
        time.sleep(5)
        
        # Click on Sign in
        sign_in = twitter.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
        sign_in.click()
        time.sleep(5)
        
        # Enter email
        enter_email = twitter.find_element(By.XPATH, value='/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        enter_email.send_keys(TWITTER_EMAIL, Keys.ENTER)
        time.sleep(5)
        
        # Enter username
        enter_username = twitter.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        enter_username.send_keys(TWITTER_USERNAME, Keys.ENTER)
        time.sleep(5)
        
        # Enter password
        enter_password = twitter.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        enter_password.send_keys(TWITTER_PASSWORD, Keys.ENTER)
        time.sleep(5)

        # Click on post button
        post = twitter.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        post.click()
        time.sleep(5)

        # Create a tweet
        tweet = twitter.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        tweet.send_keys("This is an example tweet!")
        print(f"Hey Internet Provider, why is my internet speed {self.down} down/{self.up}up when I pay for 150down/10up?!")
        
        # Submit tweet
        post_tweet = twitter.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]')
        post_tweet.click()
        
        time.sleep(20)
        self.driver.close()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

