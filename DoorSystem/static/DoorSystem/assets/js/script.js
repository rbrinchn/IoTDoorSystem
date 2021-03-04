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
    client.publish("/try/IoTSystem", message);
}
	