# from pprint import pprint
# import smtplib
# import requests
# from bs4 import BeautifulSoup
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
#
# CLIENT_ID = "98d12eb2bc6f4abf93d20965347bd6ff"
# CLIENT_SECRET = "761a8fac2c1b4602bdb1670f305f21db"
# passwordG = "Ivan1234"
# my_email = "idiomas51231@gmail.com"
# emails = {"JJCK":"campos4551@gmail.com","LILB":"antonio61231@gmail.com"}
#
# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-public",
#         redirect_uri="http://example.com",
#         client_id=CLIENT_ID,
#         client_secret=CLIENT_SECRET,
#         show_dialog=True,
#         cache_path="token1.txt"
#     )
# )
# user_id = sp.current_user()["id"]
# date = input("Which year do you want to travel to? type the date in this format YYYY-MM-DD(2021-12-07):")
# print(f"Usuarios: {emails.keys()}")
# usuario = input("Who are you pana:").upper()
# year = date.split("-")[0]
#
# response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}")
# soup = BeautifulSoup(response.text,"html.parser")
# titles = soup.select("li h3")
# songs = []
# for title in titles:
#     songs.append(title.getText().strip())
# uri_songs = []
# for song in songs:
#     query = sp.search(q=f"track:{song} year:{year}",type="track")
#     try:
#         uri = query["tracks"]["items"][0]["uri"]
#     except:
#         print("This song doesn't exists")
#     else:
#         uri_songs.append(uri)
# playlist = sp.user_playlist_create(user=user_id,name=f"{date} Billboard 100",public=True)
# url = playlist["external_urls"]["spotify"]
# sp.playlist_add_items(playlist_id=playlist["id"],items=uri_songs[0:99])
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=passwordG)
#     connection.sendmail(from_addr=my_email, to_addrs=emails[usuario],
#                         msg=f"Subject:Spotify playlist \n\n {url}", )
from random import randint

options = f"00:{randint(10, 99)}:{randint(10, 99)}:{randint(10, 99)}:{randint(10, 99)}:{randint(10, 99)}"
print(options)
