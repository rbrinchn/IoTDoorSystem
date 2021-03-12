var messageList = [];
var client = mqtt.connect('wss://public:public@public.cloud.shiftr.io', {
    clientId: 'javascript'
});

client.on('connect', function() {
    console.log('connected!');
    client.subscribe('/try/IoTSystem');
});

client.on('message', function(topic, message) {
    console.log(topic + ': ' + message.toString());
});

function sendToArduino(message) {
    document.getElementById('lock').src="/static/DoorSystem/assets/gifs/open-2.gif";
    client.publish("/try/IoTSystem", message);
    setTimeout(function(){
        document.getElementById('lock').src="/static/DoorSystem/assets/gifs/lock-2.gif";;
        }, 3000);
}
	