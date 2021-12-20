var sio = io('ws://192.168.29.98:8010', {
    transportOptions: {
        polling: {
            extraHeaders: {
                'X-Username': window.location.hash.substring(1)
            }
        }
    }
});

sio.on('connect', () => {
    console.log("connected");

});
sio.on('disconnect', () => {
    console.log("disconnected");

});
var username = ""
sio.on('broadcast_connect_success', (data) => {
    console.log(data)

});
sio.on('receive_broadcast_message', (data) => {
    console.log(data);
    var element = document.createElement("div");
    element.appendChild(document.createTextNode(data.username + " has sended the message " + data.message));
    document.getElementById('log0').appendChild(element);

});

// function sendMessage() {
//     sio.emit
// }

function sendMessage() {


    let host = location.host;

    var url = "/sendMessage";
    console.log(url)
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", url, true);
    xhttp.setRequestHeader("Content-type", "application/json");
    var data = document.getElementById('message').value;

    xhttp.send(JSON.stringify(data));
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('message').value = "";
            // var element = document.createElement("div");
            // element.appendChild(document.createTextNode(data));
            // document.getElementById('log0').appendChild(element);
        }

    };

    // alert(xmlhttp.responseText);

}