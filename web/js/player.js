function getParameterByName(name, url = window.location.href) {
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

function update_album_line() {
    document.getElementById("verLine").style.height = document.documentElement.scrollHeight.toString()+"px";
}

function open_playlist(encoded_playlist) {
    var playlist = decodeURIComponent(atob(encoded_playlist));
    eel.get_songs(playlist);
}

eel.expose(list_songs)
function list_songs(songs) {
    var table = document.getElementById("song-list");
    table.innerHTML="";
    for (const song of songs) {
        var row = table.insertRow();
        var cell = row.insertCell(0);
        cell.innerHTML = "<button id='song_button' onClick='play_song(\""+btoa(encodeURIComponent(song))+"\")'>"+song+"</button>";
    }
    update_album_line();
}

eel.expose(list_playlists);
function list_playlists(playlists) {
    for (const playlist of playlists) {
        var table = document.getElementById("playlist-list");
        var row = table.insertRow();
        var cell = row.insertCell(0);
        cell.innerHTML = "<button id='playlist_button' onClick='open_playlist(\""+btoa(encodeURIComponent(playlist))+"\")'>"+playlist+"</button>";
    }
    update_album_line();
}

function play_song(song) {
    var device = atob(getParameterByName('device'));
    song = decodeURIComponent(atob(song))
    eel.start_song(device, song)
}

window.onload = function() {
    eel.get_playlists();
}