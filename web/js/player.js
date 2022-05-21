function getParameterByName(name, url = window.location.href) {
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

function print_devices() {
    var table = document.getElementById("device-list");
    var row = table.insertRow();
    var cell = row.insertCell(0);
    var device = atob(getParameterByName('device'))
    cell.innerHTML = "<p>"+device+"</p>"
}

window.onload = function() {
    print_devices();
}