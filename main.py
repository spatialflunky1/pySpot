import eel
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import options

window_size=(1280,720)
device_names = []
eel.init("web")

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=options.scope,client_secret=options.CS,client_id=options.CID, redirect_uri=options.redirectURI))
devices = spotify.devices()
for i in range(len(devices["devices"])):
    device_names.append(devices["devices"][i]["name"])

@eel.expose
def get_devices():
    eel.list_devices(device_names)

eel.start("devices.html", size=window_size)
