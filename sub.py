# This program subscribe the message of nodes in the mesh network. The received message is saved in a text file with node id. The message starts with painless/from/12345678"
# where 12345678 is the node id of the node that has sent the message. The message includes the node name, Analog reading of pin A0 of ESP8266 and free memory present
# in ESP8266. Please enter the Local ip address of your PC/Laptop in the line with "****"
import paho.mqtt.client as mqtt
from datetime import datetime
import csv


 # The callback for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))#Print result of connection attempt
    client.subscribe("hetadatainMesh/from/+")    # Subscribe all msg having topic "painlessMesh/from/"
    
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")     
    
filename= "filename.csv"

def on_message(client, userdata, msg):
    f = open(filename, "a")
    msg.payload = msg.payload.decode("utf-8")
    #Print a received msg
    print(datetime.now().strftime('%d/%m/%y %H:%M:%S:%f')[:-5] + " " + str(msg.payload), file = f)  
    print(datetime.now().strftime('%H:%M:%S:%f')[:-7] + " " + str(msg.payload))


client = mqtt.Client()  # Create instance of client with client ID “digi_mqtt_test”
client.on_connect = on_connect  # Define callback function for successful connection
client.on_disconnect = on_disconnect # Define callback function for disconnection
client.on_message = on_message  # Define callback function for receipt of a message
client.connect("192.168.31.7", 1883, 100)  #*****
client.loop_forever() 


