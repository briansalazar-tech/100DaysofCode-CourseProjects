import requests
from bs4 import BeautifulSoup as bs

# TODO 1 Scrape Billboard Hot 100
# TODO 2 Authentication with Spotify
# TODO 3 Search Spotidy for Sings from Step 1
# TODO 4 Creating and Adding to Spotify Playlist

# date_prompt = input("Which year do you want to travel to? Type the date in the format of YYYY-MM-DD: ")
date_prompt = "2012-06-15" # Static date for testing
BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{date_prompt}"
HEADER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=BILLBOARD_URL, headers=HEADER)
soup = bs(response.text, "html.parser")

top100 = []
unformatted_song_titles = soup.select(selector="li ul li h3")
for song in unformatted_song_titles:
    song_name = song.getText().strip()
    top100.append(song_name)

print(top100)