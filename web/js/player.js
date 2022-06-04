function getParameterByName(name, url = window.location.href) {
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

function open_playlist(playlist_id) {
    eel.get_songs(playlist_id);
}

eel.expose(list_songs)
function list_songs(songs) {
    var song_list = document.getElementById("song-list");
    song_list.innerHTML="";
    const ids = [];
    const song_names = [];
    for (let i=0; i<songs.length; i++) {
        if (i%2==0) song_names.push(songs[i]);
        else ids.push(songs[i]);
    }
    for (let i=0; i<songs.length/2; i++) {
        song_list.innerHTML += "<button id='song_button' onClick='play_song(\""+ids[i]+"\")'>"+song_names[i]+"</button><br><br>";
    }
    song_list.scrollTop = document.documentElement.scrollTop = 0;
}

eel.expose(list_playlists);
function list_playlists(playlists) {
    var playlist_list = document.getElementById("playlist-list");
    const ids = [];
    const playlist_names = [];
    for (let i=0; i<playlists.length; i++) {
        if (i%2==0) playlist_names.push(playlists[i]);
        else ids.push(playlists[i]);
    }
    for (let i=0; i<playlists.length/2; i++) {
        playlist_list.innerHTML += "<button id='playlist_button' onClick='open_playlist(\""+ids[i]+"\")'>"+playlist_names[i]+"</button><br><br>";
    }
    document.getElementById("verLine").style.height = document.documentElement.scrollHeight.toString()+"px";
}

function play_song(id) {
    var device = atob(getParameterByName('device'));
    eel.start_song(device, id)
}

window.onload = function() {
    eel.get_playlists();
}