eel.expose(list_devices);
function list_devices(devices) {
    for (const device of devices) {
        var tag = document.createElement("button");
        var text = document.createTextNode(device);
        tag.appendChild(text);
        var element = document.getElementById("device_list");
        element.appendChild(tag);
    }
}

window.onload = function() {
    eel.get_devices();
};

// document.getElementById("button-temp").addEventListener("click", ()=>{eel.get_devices()}, false);
