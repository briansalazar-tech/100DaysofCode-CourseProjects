# Day 50: Tinder Swipe Bot
## Lesson Overview
For Day 50 of the 100 Days of Code course, the goal was to create an auto swipe bot for Tinder. This project, as with the previous projects, is completed using Selenium. 

*For this project, I ended up using my originally completed project as I did not want to create a Tinder account so this document will serve as a walkthrough of my original attempt.*
## Project
### Modules Used
#### Dotenv and os
**Dotenv** and **os** are used to access the environment variables used in this project.
#### Time
**Time** is used in this project to pause after each action performed. Pausing between action mimics a more human-like behavior.
#### Selenium
**Selenium** is the star of the show in this project. Selenium is used to log into Tinder and Swipe on other user’s profiles.
### Project Walkthrough
After loading the necessary modules and environment variables the first step in the project is to log into Tinder. This project uses **Facebook credentials** for logging in so those credentials are provided in **environment variables**.

After logging in the next step is to dismiss the popup windows that appear after logging in.

With the popups dismissed, we now proceed to swipe at the first 20 profiles that are displayed. In order to keep this project a bit more ethical, I made sure the bot hit the **dislike button** instead of like button.
