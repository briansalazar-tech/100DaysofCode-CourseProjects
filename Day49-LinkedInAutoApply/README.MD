# Day 49: LinkedIn Auto Apply
## Lesson Overview
The project **for Day 49** is to create a bot that auto-applies to jobs on LinkedIn that have the “**Easy apply**" button.  For today’s project, I ended up using my code from my original attempt for this project. When I initially completed this project, instead of applying for a job, I **saved** the job to be applied for later.

*This readme serves as a walkthrough of my original attempt at this project*.
## Project
### Modules Used
#### Dotenv and os
**Dotenv** and **os** are used to access the environment variables used in this project.
#### Selenium
**Selenium** is the focus of this lesson; Selenium is used to log in to LinkedIn and apply to jobs. Or in my case, save jobs.
#### Time
**Time** is used in this program to pause each iteration through the job listings. Pausing between each job mimics a more human-like behavior.
### Project Walkthrough
The first step in this project is to log in to LinkedIn. The **job search results** page is passed as the **URL to open**. Since the user is not logged into LinkedIn, Selenium finds the **sign-in button** and enters the saved **username** and **password** in the appropriate fields.

Once logged in, a **try/except** loop is used to minimize the **messages tab** if it is expanded.

With that, the next step is to loop through the job search results and save the jobs! **Find_elements()** gets all the list items for the job search return. A **For loop** is used to get the **id attribute** for each job that is saved. Afterwards, a separate **For loop** is used to **filter** out jobs that have a **blank id value**. With the necessary data, all that remains is to click the **save button** using one last **For loop**. For one additional challenge, each iteration also **follows** the **company** that posted the job.