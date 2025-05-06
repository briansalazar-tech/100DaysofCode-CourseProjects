from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Get total number of artlcles from Wikipedia homepage
# Solution used By.CSS_Selector (#articlecount li) ~ At time of practice, two li objects under articlecount
# articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# print(articles.text)
# articles.click() # Clicks on an element

# all_portals = driver.find_element(By.LINK_TEXT, value="Community portal") # Finds an element by the link text value

# Text box field
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER) # Types Python in the search field and presses enter

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Brian")
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Salazar")
email = driver.find_element(By.NAME, value="email")
email.send_keys("someone@email.com")
button = driver.find_element(By.CLASS_NAME, value="btn")
button.click()




# driver.quit()

