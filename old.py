from tkinter import *
import options
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
import json

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=options.scope,client_secret=options.CS,client_id=options.CID, redirect_uri=options.redirectURI))
devices = spotify.devices()

root = Tk()
root.title("Spotify: Devices")
canvas = Canvas(root, height=200)
frame = Frame(canvas)
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
canvas.pack(side=LEFT, fill=Y, expand=True)
canvas.create_window((4,4), window=frame, anchor="nw", tags="frame")
frame.bind("<Configure>", lambda x: canvas.configure(scrollregion=canvas.bbox("all")))
root.bind("<Down>", lambda x: canvas.yview_scroll(3, 'units'))
root.bind("<Up>", lambda x: canvas.yview_scroll(-3, 'units'))
root.bind("<MouseWheel>", lambda x: canvas.yview_scroll(int(-1*(x.delta/40)), "units"))

def allPlaylists(DeviceID):
    allPlaylistsWindow = Toplevel(root)
    allPlaylistsWindow.title("Spotify: Albums")
    canvas = Canvas(allPlaylistsWindow, height=200)
    frame = Frame(canvas)
    scrollbar = Scrollbar(allPlaylistsWindow, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side=LEFT, fill=Y, expand=True)
    canvas.create_window((4,4), window=frame, anchor="nw", tags="frame")
    frame.bind("<Configure>", lambda x: canvas.configure(scrollregion=canvas.bbox("all")))
    allPlaylistsWindow.bind("<Down>", lambda x: canvas.yview_scroll(3, 'units'))
    allPlaylistsWindow.bind("<Up>", lambda x: canvas.yview_scroll(-3, 'units'))
    allPlaylistsWindow.bind("<MouseWheel>", lambda x: canvas.yview_scroll(int(-1*(x.delta/40)), "units"))

    playlists = spotify.current_user_playlists()
    playlasts = playlists["items"]
    while playlists["next"]:
        playlists = spotify.next(playlists)
        playlasts.extend(playlists["items"])
    x = len(playlasts[0]["name"])
    z = 0
    playButtons = []
    frame.columnconfigure(0, weight=1)
    for i in playlasts:
        l = Button(frame, text=str(i["name"]), command=lambda i=i: playlistWindow(i["name"], i["uri"], DeviceID))
        if len(i["name"]) > x:
            x = len(i["name"])
        playButtons.append(l)
        l.grid(row=z, column=0, sticky=W)
        z += 1
    x = int(x * 6.5)
    allPlaylistsWindow.geometry(str(x)+"x600")
    allPlaylistsWindow.config(bg="black")
    frame.config(bg="black")
    canvas.config(bg="black")

def playlistWindow(name, URI, DeviceID):
    ID = URI.split(":")[-1]
    playwindow = Toplevel(root)
    playwindow.title("Spotify Album: "+ name)
    canvas = Canvas(playwindow, height=200)
    frame = Frame(canvas)
    frame.pack(fill=X, side=TOP)
    scrollbar = Scrollbar(playwindow, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=frame, anchor="nw", tags="frame")
    frame.bind("<Configure>", lambda x: canvas.configure(scrollregion=canvas.bbox("all")))
    playwindow.bind("<Down>", lambda x: canvas.yview_scroll(3, 'units'))
    playwindow.bind("<Up>", lambda x: canvas.yview_scroll(-3, 'units'))
    playwindow.bind("<MouseWheel>", lambda x: canvas.yview_scroll(int(-1*(x.delta/40)), "units"))
    results = spotify.user_playlist_tracks("kandrus71",ID)
    tracks = results['items']
    x = len(tracks[0]["track"]["name"])
    while results['next']:
        results = spotify.next(results)
        tracks.extend(results['items'])
    z=0
    songs = []
    for song in tracks:
        if song["track"] != None:
            s = Button(frame, text=str(song["track"]["name"]), command=lambda song=song: playSong(song["track"]["name"], [song["track"]["uri"]], DeviceID))
            if len(song["track"]["name"]) > x:
                x = len(song["track"]["name"])
            songs.append(song)
            s.grid(row=z, column=0, sticky=W)
            z+=1
    print("# of songs: ", z)
    x = int(x * 6.5)
    playwindow.geometry(str(x)+"x600")
    playwindow.config(bg="black")
    frame.config(bg="black")
    canvas.config(bg="black")

def playSong(name, URI, DeviceID):
    print("Now Playing: ", name)
    print(DeviceID)
    try:
        spotify.start_playback(DeviceID, None, URI)
    except:
        print(URI)

root.config(bg="black")
frame.config(bg="black")
canvas.config(bg="black")
z = 0
deviceButtons = []
x = len(devices["devices"][0]["name"])
for i in range(len(devices["devices"])):
    # print(i, ": ", devices["devices"][i]["name"])
    l = Button(frame, text=str(devices["devices"][i]["name"]), command=lambda i=i: allPlaylists(devices["devices"][i]["id"]))
    if len(devices["devices"][0]["name"]) > x:
        x = len(devices["devices"][0]["name"])
    deviceButtons.append(l)
    l.grid(row=z, column=0, sticky=W)
    z += 1
x = int(x * 6.5)   
root.geometry(str(x) + "x200")
root.mainloop()