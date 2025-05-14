# Day 51: Internet Speed Complaint Bot
## Lesson Overview
The project for **day 51** was to create a **Twitter (X) complaint bot**. The event that triggers the complaint is when an internet speed test falls under a specified threshold. If the speed falls below that threshold, a Twitter post raises the complaint.

*As with the previous lessons on web scraping, I decided to use my original completion of this project, and this documentation will serve as a walkthrough of that project.*
## Project
### Modules Used
#### Os & dotenv
**Dotenv** and os are used to access the environment variables used in this project.
#### Time
**Time** is used in this project to pause after each action is performed. Pausing between actions mimics a more human-like behavior. Additionally, this pause is needed to execute the internet speed test.
#### Selenium
**Selenium** is the star of the show in this project. Selenium is used to execute the internet speed test and make a Twitter post when the internet speed threshold is not met.
### Project Walkthrough
This project uses several constants to make a Twitter post. Below is an overview of what they accomplish:
-	**PROMISED_UP** and **PROMISED_DOWN**: Thresholds for promised upload and download speeds.
-	**TWITTER_EMAIL**, **TWITTER_USERNAME**, and **TWITTER_PASSWORD**: These constants are used to log into Twitter.

Unlike the previous two projects, this project is completed using a class with two methods. The **InternetSpeedTwitterBot** class has two methods. 
-	**Get_internet_speed**: The get internet speed class is first called to execute an internet speed test using the specified URL. The method has a 75 second pause to allow the internet speed test to finish running. After the test is finished running, the class’s **up** and **down attributes** are updated with the values returned by the speed test. With the attributes updated, the bot waits two minutes before closing the window.
-	**Tweet_at_provider**: The tweet at provider class is called after the **Get_Internet_speed** method to make a Twitter post complaining about the results of the internet speed test. First, the method logs into Twitter using the constants listed above. After logging in, a Twitter post is made. Once 20 seconds have passed, Chrome is closed.

The **InternetSpeedTwitterBot** class could have been created in its own file, however, all the code exists in main.py. With three additional lines, the object is created, and the two methods listed above are executed!

