from selenium import webdriver
from selenium.webdriver.common.by import By
# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.google.com")
driver.get("https://www.python.org/")


price_dollar = driver.find_element(By.CLASS_NAME, vallue="a-price-whole") # Retreives the HTML element by class name
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}") # .text is needed 

search_bar = driver.find_element(By.NAME, value="q") # Selects the item based on its name, which is q
# print(search_bar.tag_name) # Returns the HTML tag name
# print(search_bar.get_attribute("placeholder")) # Gets the attribute value for an attribute named 

button = driver.find_element(By.ID, value="submit") # Selects an element with the value of submit
# print(button.size) # Returns the elements dimensions 

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a") # Selects an a tag inside a div with the class of documentation widget
#print(documentation_link.text)

# Find element by x-path - If finding via selector does not work, use x-path
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a') # Walks path to the specific element you want to select
#print(bug_link.text)

# Find Elements by CSS Selector
driver.find_elements(By.NAME, value="") # Returns an entire list of the elements that have the given name. Same as previous examples, except returns more than 1

events = {}

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time") # Select by CSS Selector (Class and element)
# for time in event_times:
#     print(time.text)

event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# for event in event_names:
#     print(event.text)

for n in range(len(event_times)):
    events[n] = {
        "time": event_names[n].text,
        "name": event_names[n].text,
    }

print(events)


# driver.close() # Closes single tab
driver.quit() # Quitz the entire browser