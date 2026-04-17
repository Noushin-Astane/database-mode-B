import json
import paho.mqtt.client as mqtt
from sqlidb import save_to_sqlite
from mongodb import save_to_mongodb
from neo4jdb import save_to_neo4j

def on_message(client, userdata, message): #mqtt/subscriber/recieve message from broker zzzzzanzara 
    payload = json.loads(message.payload.decode("utf-8")) #message.payload you recieve messages in bytes .decode convert byts in string*
    sensor_type = payload.get("type") #this payload is built-in mqtt attribute **
    print(f"Received: {payload}")

    if sensor_type == "temperature":
        save_to_sqlite(payload) #send the dictionary to sqlite
        print("Temperature saved to SQLite 🌶️")

    elif sensor_type == "humidity":
        save_to_sqlite(payload)
        print("Humidity saved to SQLite 🐮")

    elif sensor_type == "air_quality":
        save_to_mongodb(payload)
        print("Air quality saved to MongoDB 🐭")

    elif sensor_type == "Co2":
        save_to_neo4j(payload)
        print("CO2 saved to Neo4j 🐷 ")

    else:
        print(f"Unknown sensor type: {sensor_type}")

client = mqtt.Client()
client.connect("localhost", 1883)
client.subscribe("env/#")
client.on_message = on_message

print("Listening for sensor data...")
client.loop_forever()

#something that you havfe to remember and pay attention gurrl is that payload ⭐
#** basically mqtt says: here the raw content of message. ⭐
#why i had to declair the varible "payload"& get confused alot over it?IDK,giorgio said,i think it's stupid, remember to ask or search later why:| 
#remember publisher doesnt care where you save your data it just generates the data the subscriber care where you are saving your data bases 