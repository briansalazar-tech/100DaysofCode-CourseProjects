# Day 52: Instagram Follower Bot
## Lesson Overview
For **day 52**, the goal is to create an **Instagram follower bot**. After finding an account, the program lists the account’s followers and follows all the account’s following the account.

*As with the previous projects working with Selenium and web scraping, I decided to use my original completion of this project. This document will serve as a walkthrough of that project.*
## Project
### Modules Used
#### Os & dotenv
**Dotenv** and **os** are used to access the environment variables used in this project.
#### Selenium
**Selenium** is used to log into Instagram, search for an account, and follow that account’s followers.
#### Time
**Time** is used in this project to pause after actions are performed. Pausing between actions mimics a more human-like behavior and allows pages to load completely. 
### Project Walkthrough
After loading the necessary modules and environment variables, this program creates a class called **InstagramBot**. The **InstagramBot** class is used to carry out all the functionality of this project within the class. After the bot object is created, the bot logs in and finds the followers to follow! With that, that completes the project!

Within the class the following methods are used to achieve the end goal above:
-	**Login**: Login is used to log into the user’s Instagram account with the credentials saved using environment variables.
-	**Follow**: Follow does as the name implies. Follow is used to click on the follow button for an account. The follow method is called within the **find_followers** method.
-	**Find_followers**: Find followers makes up the bulk of the code in the InstagramBot class. The method dismisses popups, searches for the search bar, and searches for the account to find their followers. After selecting the account, the InstagramBot clicks on the following button and iterates through the list of followers returned and clicks the follow button next to the account.
