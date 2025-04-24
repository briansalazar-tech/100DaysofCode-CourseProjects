import requests
import spotipy
import os
from pprint import pprint
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv

load_dotenv()

date_prompt = input("Which year do you want to travel to? Type the date in the format of YYYY-MM-DD: ")
# date_prompt = "2012-06-15" # Static date for testing
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
    username="31vnv3a5ucjw7b3eh22dhuaa5npm",
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

song_uris = ['spotify:track:1VF1RJ9vJMixaf17rGmR77', 'spotify:track:4wyuCvdRgicTGn5dJTeHoP', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:53s3rQ5sk26p75z7OiSwfR', 'spotify:track:6siCcsHzddaLJiVUfIa1g3', 'spotify:track:23AA2RqAweZ9bv0zX2fkka', 'spotify:track:32ZSwmYdWfAQsHO1sM1LQM', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:6yVpxVBp6WpfJemcxUSWco', 'spotify:track:5ECctRJpndFvwFhuqJTpQs', 'spotify:track:3mwyEHi0EoyQ1GbsMNk88v', 'spotify:track:3mwyEHi0EoyQ1GbsMNk88v', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:25dX0AxixYj6gbsbIS5qFz', 'spotify:track:2Gu7lVRhWwAo9BJt0KyRqJ', 'spotify:track:1iUsJr7Poavlvrt85L1l7q', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:6ycus2Yb546WD4OXLbIM2P', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:0d28khcov6AiegSCpG5TuT', 'spotify:track:0jv5VgdENAPV7lHtBlsaXE', 'spotify:track:4wyuCvdRgicTGn5dJTeHoP', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:1WoN9wjxZSpqwqnH9ApaGi', 'spotify:track:65Wldc6ys50dChWVHXyL3b', 'spotify:track:22YU9qmgjEtcylKMty37C6', 'spotify:track:6Lq1X5hPJk1sEMoJPR0mkS', 'spotify:track:7wg4grh9Bvme8vn29JvWQE', 'spotify:track:5NyfA8UvFew8euxEYGppSo', 'spotify:track:4H0sinchz1abeOnRCPx5mr', 'spotify:track:187N0YdCe2p3CG2C2ONLuK', 'spotify:track:2CUta3LuLFP2nZXyEoQarK', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:6Vecwo7AHst9V2CE3kmwr0', 'spotify:track:6syQaBf8Chi5BBTrulHDux', 'spotify:track:29vxkoDeEXaW7cFcNn0Ikh', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:6NLwnzxHar0ObX2gzCkv1t', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:3mwyEHi0EoyQ1GbsMNk88v', 'spotify:track:24P77koWrDCSIJpTbRTFp8', 'spotify:track:0gSoEBU9V2X2MaVSIQMNiV', 'spotify:track:3mwyEHi0EoyQ1GbsMNk88v', 'spotify:track:7BRGpPxMxteyBMdACh7D2p', 'spotify:track:3McWfs2QJO0nkYOwi8gyPO', 'spotify:track:29vxkoDeEXaW7cFcNn0Ikh', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:0wps7rop5iHwBo0rQZ2g9A', 'spotify:track:3mwyEHi0EoyQ1GbsMNk88v', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:29vxkoDeEXaW7cFcNn0Ikh', 'spotify:track:6nM3c7vp11v9M5ExeqnZWL', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:3mwyEHi0EoyQ1GbsMNk88v', 'spotify:track:2h5wkA3keIclvfAJ95VMAo', 'spotify:track:0d28khcov6AiegSCpG5TuT', 'spotify:track:29vxkoDeEXaW7cFcNn0Ikh', 'spotify:track:0HVxNjgwLQpqLyREsgJ1Rh', 'spotify:track:0sX20wyF4lxE5HJaJr0IjO', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:1SXbZ8QmeRP4vU3LzVsvhw', 'spotify:track:0PXfz96ntL8C8df4mrmm6z', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:5BRfY9GjQCM0bs9Gq2Z1TO', 'spotify:track:2aQIkdVeVp5VcEmtIxQ2Wt', 'spotify:track:29vxkoDeEXaW7cFcNn0Ikh', 'spotify:track:0PXfz96ntL8C8df4mrmm6z', 'spotify:track:1sttCoY0ge1wtnMOsu0r6b', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:1hKKpoxY40aTVVvq4IatoD', 'spotify:track:02odT3uP8mH1y3oIk1CoEw', 'spotify:track:0PXfz96ntL8C8df4mrmm6z', 'spotify:track:0PXfz96ntL8C8df4mrmm6z', 'spotify:track:6g58NcIhNb2trd8dzVQjoA', 'spotify:track:0vI2WZx4xoOK9Eybivd7HQ', 'spotify:track:2h5wkA3keIclvfAJ95VMAo', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:4wlcESi0uaBK3Z2S1D5TUj', 'spotify:track:0PXfz96ntL8C8df4mrmm6z', 'spotify:track:0wps7rop5iHwBo0rQZ2g9A', 'spotify:track:0NEsINvKVUJ0GpE9cu0DOd', 'spotify:track:7EYw4EqnXvY4YaeAnDF0W6', 'spotify:track:7J0RBtpBxBVAmTQ2XIWo56', 'spotify:track:3YK8ALxbqymzAoHo7twtoB', 'spotify:track:6r8tUUbKKGPIfiQKPsQqn0', 'spotify:track:1YWNHUhOGcTc9rpAbyJDgL', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:29m5ZE0vd9nhXmEQnYa0aA', 'spotify:track:6bUELGn6YFR92JbBEoz39Z', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:1iUsJr7Poavlvrt85L1l7q', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:3mwyEHi0EoyQ1GbsMNk88v', 'spotify:track:6sC4ML9ZdhLT83ELUILdSf', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw', 'spotify:track:0Qu9sjpB7etQJYPGmJwdZw']

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