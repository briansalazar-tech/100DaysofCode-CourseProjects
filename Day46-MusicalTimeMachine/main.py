import requests
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv

# TODO 3 Search Spotidy for Sings from Step 1
# TODO 4 Creating and Adding to Spotify Playlist

load_dotenv()

# date_prompt = input("Which year do you want to travel to? Type the date in the format of YYYY-MM-DD: ")
date_prompt = "2012-06-15" # Static date for testing
BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{date_prompt}"
HEADER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_KEY")
REDIRECT_URI = "https://example.com"
USERNAME=os.getenv("SPOTIFY_USERNAME")

# response = requests.get(url=BILLBOARD_URL, headers=HEADER)
# billboard_site = response.text
# soup = bs(billboard_site, "html.parser")

# top100 = []
# unformatted_song_titles = soup.select(selector="li ul li h3")
# for song in unformatted_song_titles:
#     song_name = song.getText().strip()
#     top100.append(song_name)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="./Day46-MusicalTimeMachine/token.txt",
    username="31vnv3a5ucjw7b3eh22dhuaa5npm",
))

user_id = sp.current_user()["id"]