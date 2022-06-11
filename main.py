import requests
import os
import spotipy
import bs4
import pprint


#redirect_url_return = https://example.com/callback?code=AQDs5elZ9O5HniBY3drlm8dCfHpmUP0NbZ7UQLkkTVz4QK6Vj0er7_c7p66cuclClw64dAguUrICQUKHlxT3TYYarDMJqLKOA71XwGgQyaPG531xIIhxqWAEfEvAuwQVTzX92R2x4t16oSDatj5LIaj4V39zv66lr52zuuEjYh1j2ZZqUdJUnldA8K1A8znR4qBbPnKjj5F_
date = input("What day do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# date = "2010-05-22"
url = f"https://www.billboard.com/charts/hot-100/{date}/"

html_billboard = requests.get(url).text

soup = bs4.BeautifulSoup(html_billboard, "html.parser")

song_selector = "div ul li ul li h3"

print(soup.select_one(selector=song_selector).get_text().strip())

# print(soup.find(name="h3", id="title-of-a-story").get_text().strip())


list_of_song_titles = [tag.get_text().strip() for tag in soup.select(selector=song_selector)]

print(list_of_song_titles)
print(os.environ.get("SPOTIPY_REDIRECT_URI"))

spoti = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
                                                                 client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
                                                                 redirect_uri=os.environ.get("SPOTIPY_REDIRECT_URI"),
                                                                 scope="playlist-modify-private",
                                                                 show_dialog=True,
                                                                 cache_path="token.txt"))

print("*****************")
print(spoti)
user_id = spoti.current_user()
# pprinter = pprint.PrettyPrinter()
# pprinter.pprint(spoti)
# print(spoti.)
# playlist = spoti.user_playlist_create(user=os.environ.get("SPOTIPY_CLIENT_ID"), name="ToppiesOf2021", public=False, collaborative=False, description="2021 playlist")
# print(playlist)

# pprint.pprint(spoti)