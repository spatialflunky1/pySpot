eel.expose(list_devices);
function list_devices(devices) {
    for (const device of devices) {
        var table = document.getElementById("device-list");
        var row = table.insertRow();
        var cell = row.insertCell(0);
        cell.innerHTML = "<button id='button'>"+device+"</button>"
    }
}

window.onload = function() {
    eel.get_devices();
};

// document.getElementById("button-temp").addEventListener("click", ()=>{eel.get_devices()}, false);
