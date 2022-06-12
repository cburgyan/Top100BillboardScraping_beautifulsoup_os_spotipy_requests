import requests
import os
import spotipy
import bs4
import pprint


#Get Date of interest from user
date = input("What day do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# date = "2010-05-22"


#Get Top 100 songs list from billboard
url = f"https://www.billboard.com/charts/hot-100/{date}/"
html_billboard = requests.get(url).text
soup = bs4.BeautifulSoup(html_billboard, "html.parser")
song_selector = "div ul li ul li h3"
print(soup.select_one(selector=song_selector).get_text().strip())
# print(soup.find(name="h3", id="title-of-a-story").get_text().strip())
list_of_song_titles = [tag.get_text().strip() for tag in soup.select(selector=song_selector)]
print(list_of_song_titles)


#Get spotify authentication
# print(os.environ.get("SPOTIPY_REDIRECT_URI"))
spoti = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
                                                                 client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
                                                                 redirect_uri=os.environ.get("SPOTIPY_REDIRECT_URI"),
                                                                 scope="playlist-modify-private",
                                                                 show_dialog=True,
                                                                 cache_path="token.txt"))

print("*****************")
print(spoti)


#Get spotify user id
user_id = spoti.current_user()["id"]
print(user_id)
# print(date[:4])


#Get song URIs
song_uri_list = []
# printed_one = False
for song in list_of_song_titles:
    parameters = f"track:{song} year:{date[:4]}"
    search_result = spoti.search(q=parameters, type="track")
    # if not printed_one:
    #     pprint.pprint(search_result)
    #     printed_one = True
    try:
        song_uri = search_result["tracks"]["items"][0]["uri"]
        song_uri_list.append(song_uri)
    except IndexError:
        print(f'"{song}" is not in Spotify inventory.')
    else:
        print(song)


#Create and fill playlist
playlist = spoti.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False, collaborative=False, description="2021 playlist")
# print(type(playlist))
# print(playlist)
# print(playlist["id"])
# print(playlist["uri"])
response = spoti.playlist_add_items(playlist_id=playlist["id"], items=song_uri_list)
print(type(response))
pprint.pprint(response)
