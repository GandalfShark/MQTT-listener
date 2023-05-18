"""
MQTT listener 
based on code from links below:
https://morphuslabs.com/hacking-the-iot-with-mqtt-8edaf0d07b9b
https://github.com/eclipse/paho.mqtt.python#installation

useful in CTF:
https://tryhackme.com/room/bugged

Author: Gandalf Sharkmeister the first of his name, 
        King of Bupkis and protector of the realm.

*nix=true, win=gtfo
"""
import paho.mqtt.client as mqtt
print("""
. . . . . . . .

MQTT - Listener 

. . . . . . . .
""")
target = input('Enter Target IP: ')
# no error checking :P
vom_file_name = input('Enter output file name: ')

def on_connect(client, userdata, flags, rc):
    print ('[+] Connection successful, code: '+str(rc))
    client.subscribe('#', qos = 1)        
    # Subscribe to all topics
    client.subscribe('$SYS/#')            
    # Broker Status (Mosquitto)
   
def on_message(client, userdata, msg):
    top = msg.topic
    pay = msg.payload
    with open (f'{vom_file_name}.txt', 'a') as f:
        print(f'TOPIC: {top}, PAYLOAD: {pay}', file=f)
    print('topic and payload written to file\n')
    print(f'TOPIC: {top}, PAYLOAD: {pay}')
    # vomit the data into a file and display it on screen

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect((f'{target}'), 1883, 60)

client.loop_forever() 	
