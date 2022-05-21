eel.expose(list_devices);
function list_devices(devices) {
    for (const device of devices) {
        var table = document.getElementById("device-list");
        var row = table.insertRow();
        var cell = row.insertCell(0);
        var encoded_device=btoa(device);
        cell.innerHTML = "<button id='button' onClick='open_player(\""+encoded_device+"\")'>"+device+"</button>"
    }
}

function open_player(encoded_device) {
    location.href = "player.html?device="+encoded_device;
}

window.onload = function() {
    eel.get_devices();
};
