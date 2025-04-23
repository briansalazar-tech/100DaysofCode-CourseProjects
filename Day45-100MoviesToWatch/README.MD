[empiresite]: https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/
# Day 45: 100 Movies to Watch
## Lesson Overview
**Day 45** moves from HTML and CSS introductions to working with Beautiful Soup and web scraping. The concepts covered in this lesson include the following:
-	Introduction to **BeautifulSoup**
-	Ethics of **web scraping** & **Robots.txt**
## Project
### Modules Used
#### Requests
**Requests** is used to get the contents of the internet archive URL for the 100 movies to watch.
#### BeautifulSoup
**BeautifulSoup** is used to parse through the list of movies to watch and get the movie titles.
### Project Walkthrough
This project aims to create a text file of 100 movies to watch according to Empire Online. 

This project first starts by using **requests** to get the contents of the [EmpireOnline.com movies to watch web page][empiresite] (internet archive link). The response is then passed into **BeautifulSoup** so that the contents can be parsed.

Utilizing a couple of classes in the HTML code, the titles of the 100 movies to watch are added to a list. Since the movies are ranked from 100 to 1, a separate list is created to rank the movies from 1 to 100 before adding them to a text file.

With the movies listed in the proper order, a text file is created, and the contents of the list are appended to the new text file. 
