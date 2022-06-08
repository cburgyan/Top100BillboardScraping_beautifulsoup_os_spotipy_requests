import requests
import os
import spotipy
import bs4


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

spoti = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
                                                                 client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
                                                                 redirect_uri=os.environ.get("SPOTIPY_REDIRECT_URI"),
                                                                 scope="playlist-modify-private",
                                                                 show_dialog=True,
                                                                 cache_path="token.txt"))


print(spoti)