import requests
import spotipy
import os
from pprint import pprint
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv

load_dotenv()

date_prompt = input("Which year do you want to travel to? Type the date in the format of YYYY-MM-DD: ")

BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{date_prompt}"
HEADER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_KEY")
REDIRECT_URI = "https://example.com"
USERNAME=os.getenv("SPOTIFY_USERNAME")

## Create soup of Billboard Top 100 songs for date
print("Connecting to Billboards Top 100 URL")
response = requests.get(url=BILLBOARD_URL, headers=HEADER)
billboard_site = response.text
soup = bs(billboard_site, "html.parser")

## Create list of top 100 songs
print("Creating list of top 100 song names")
top100 = []
unformatted_song_titles = soup.select(selector="li ul li h3")
for song in unformatted_song_titles:
    song_name = song.getText().strip()
    top100.append(song_name)

##  Connect to Spotify with Spotipy
print("Connecting to Spotify")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="./Day46-MusicalTimeMachine/token.txt",
    username=os.getenv("SPOTIFY_USERNAME"),
))

user_id = sp.current_user()["id"]

## Search for song URIs
print("Searching for URIs of songs...")
song_uris = []
for song in top100:
    print(f"Search for: {song}")
    try:
        results = sp.search(q=f"track: {song} year: {date_prompt.split("-")[0]}", limit=1)
        try:
            song_uri = results["tracks"]["items"][0]["uri"]
            song_uris.append(song_uri)
        except:
            print("No results for song")
    except:
        print("TimeoutError or other error retreiving song. Continuing...")

# Create private playlist
playlist_name = f"Billboard 100 for {date_prompt}"
print(f"Creating playlist titled: {playlist_name}")
create_playlist = sp.user_playlist_create(
    user=user_id,
    name=playlist_name,
    public=False,
    description=f"Playlist of songs from the Billboard Top 100 for {date_prompt}",
)
playlist_id = create_playlist["id"]
print(playlist_id)

## Add songs to private playlist
print("Adding songs to playlist")
sp.playlist_add_items(
    playlist_id=playlist_id,
    items=song_uris
)

print("Playlist created and songs added successfully!")