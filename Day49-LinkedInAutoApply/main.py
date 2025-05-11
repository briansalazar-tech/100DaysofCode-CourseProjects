from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

JOB_PAGE = "https://www.linkedin.com/jobs/search/?currentJobId=3702818809&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"
LINKEDIN_EMAIL = ""
LINKEDIN_PASSWORD = None

# Open the URL with preconfigured job settings (While signed out)
driver.get(url=JOB_PAGE)
time.sleep(5)

# Click Sign In Button
sign_in_button = driver.find_element(By.LINK_TEXT, value='Sign in')
sign_in_button.click()
time.sleep(5)
# Username and password
username = driver.find_element(By.ID, value="username")
username.click()
username.send_keys(LINKEDIN_EMAIL)
time.sleep(2)
password = driver.find_element(By.ID, value="password")
password.click()
password.send_keys(LINKEDIN_PASSWORD, Keys.ENTER)
time.sleep(15)

try:
    # XPATH to down arrow button for Linkedin messages. ember## value changes from 39-41 during multiple runs
    close_messages = driver.find_element(By.XPATH, value='/html/body/div[5]/div[4]/aside[1]/div[1]/header/div[3]/button[2]')
    close_messages.click()
    time.sleep(2)
except:
    close_messages = driver.find_element(By.ID, value="ember41")
    close_messages.click()
    time.sleep(2)
# selects the list of all jobs. All jobs are passed to empty list
get_all_jobs = driver.find_elements(By.CSS_SELECTOR, value=" .scaffold-layout li")
ember_unfiltered = []
# Loop used to populate the unfiltered list. Note that "" entries are also added to list.
for job in get_all_jobs:
    job_id = job.get_attribute("id")
    ember_unfiltered.append(job_id)

ember_list = []
# For loop is used to filter out "" entries and append actual ember## entries to the new ember list
for id in ember_unfiltered:
    if id != "":
        ember_list.append(id)
print(ember_list)
# Entires in ember list are passed through web driver and clicked on. Last three entries are excluded as they are not actual job entries
for item in ember_list[0:-3]:
    print(item)
    select_job = driver.find_element(By.ID, value=item)
    select_job.click()
    time.sleep(2)
    # Save jobs
    save_job = driver.find_element(By.CSS_SELECTOR, value=".jobs-save-button")
    save_job.click()
    print("Job Saved")
    time.sleep(2)
    # Follow companies. Note, message box has to be closed in order for option to follow to work
    follow_company = driver.find_element(By.CLASS_NAME, value="follow")
    follow_company.click()
    # Apply to all jobs
    print("Company Followed")
    time.sleep(2)

# Close Chrome
print("Chrome is closing...")
time.sleep(5)
driver.quit()