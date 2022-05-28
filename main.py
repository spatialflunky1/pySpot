import eel
from soupsieve import select
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import options
import json

window_size=(1280,720)
device_names = []
eel.init("web")

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=options.scope,client_secret=options.CS,client_id=options.CID, redirect_uri=options.redirectURI))
devices = spotify.devices()
for i in range(len(devices["devices"])):
    device_names.append(devices["devices"][i]["name"])

playlists = spotify.current_user_playlists()
playlists2 = playlists["items"]
while playlists["next"]:
    playlists = spotify.next(playlists)
    playlists2.extend(playlists["items"])

@eel.expose
def get_devices():
    eel.list_devices(device_names)

@eel.expose
def get_playlists():
    playlistsx = []
    for i in range(len(playlists2)):
        name = playlists2[i]["name"]
        if len(name) >=30:
            name=name[0:28]
            name += "..."
        playlistsx.append(name)
    eel.list_playlists(playlistsx)

@eel.expose
def get_songs(playlist):
    songs = []
    ID = ""
    for i in playlists2:
        if i["name"] == playlist:
            ID = i["uri"].split(":")[-1]
            break
    results = spotify.user_playlist_tracks("kandrus71",ID)
    tracks = results["items"]
    while results['next']:
        results = spotify.next(results)
        tracks.extend(results['items'])
    for song in tracks:
        if song["track"] != None:
            songs.append(song["track"]["name"])
    eel.list_songs(songs)

eel.start("devices.html", size=window_size)
