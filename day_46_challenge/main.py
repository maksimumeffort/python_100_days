import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint


import requests
from bs4 import BeautifulSoup

# ----------------------SCRAPER------------------------ #

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
billboard_data = response.text

soup = BeautifulSoup(billboard_data, "html.parser")
songs = soup.select(selector="ul li h3.c-title")
song_list = [song.get_text().strip() for song in songs]
singers = soup.find_all(name="span", class_="a-no-trucate")
singer_list = [singer.get_text().strip() for singer in singers]
songs_singers = [[song_list[i], singer_list[i]] for i in range(len(song_list))]

# ----------------------SPOTIFY------------------------ #

scope = "playlist-modify-public playlist-modify-private user-top-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

user = sp.current_user()
user_id = user["id"]

uri_list = []

# populating uri_list with song uri for each value in scraped list
for s in songs_singers:
    song_query = f"track: {s[0]}, artist: {s[1]}"
    try:
        song_uri = sp.search(q=song_query, limit=1)['tracks']['items'][0]['uri']
    except IndexError:
        song_uri = None
    else:
        uri_list.append(song_uri)

# delete all playlists
playlists = sp.user_playlists(user_id)
if len(playlists) > 0:
    for playlist in playlists["items"]:
        sp.current_user_unfollow_playlist(playlist_id=playlist["id"])

print("Finished deleting unwanted playlists")

new_playlist = sp.user_playlist_create(user_id, name=f"{date} Billboard 100")

sp.playlist_add_items(new_playlist["id"], items=uri_list)





