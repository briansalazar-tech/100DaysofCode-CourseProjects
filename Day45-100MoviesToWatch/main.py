import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Get web page content
response = requests.get(url=URL)
movies_page = response.text
soup = BeautifulSoup(movies_page, "html.parser")

# Gets the movie titles and appends them to list_of_movies
list_of_movies = []
archive_titles = soup.select(selector=".article-title-description__text .title")

for movie in archive_titles:
    list_of_movies.append(movie.getText())

# Reverse the list of movies to start from 1
list_1to100 = list_of_movies[::-1]

# Create text file with list of movies
for movie in list_1to100:
    print(movie)
    with open(file="./Day45-100MoviesToWatch/100MoviesToWatch.txt", mode="a", encoding="utf-8") as file:
        file.write(f"{movie}\n")
        print("Movie added...")