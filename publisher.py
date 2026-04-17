import time     #add delays, here i chose every 5 sec 
import json     #converts the python dictionaries into json format
import random   #random generates fake values
from datetime import datetime
import paho.mqtt.client as mqtt 

client = mqtt.Client() #in this way i can connect to zanzara(broker)
client.connect("localhost", 1883) #1883 is the default mqtt port number 

while True: #publisher is always working, going through data every 5 seconds thats why we have to use while loop, while true gives us infinite loop 
    temp_data = {
        "value": round(random.uniform(15.0, 35.0), 1), #generate data between 14 and 35 :) you got this
        "unit": "C",
        "timestamp": datetime.now().isoformat(),
        "type": "temperature"
    }
    humidity_data = {
        "value": round(random.uniform(30.0, 90.0), 1),
        "unit": "%",
        "timestamp": datetime.now().isoformat(),
        "type": "humidity"
    }
    air_data = {
        "value": round(random.uniform(10, 100), 1),
        "unit": "ppm",
        "timestamp": datetime.now().isoformat(),
        "type": "air_quality"
    }
    Co2_data = {
        "value": round(random.uniform(300, 2000), 1),
        "unit": "ppm",
        "timestamp": datetime.now().isoformat(),
        "type": "Co2",
        "sensor_id": random.randint(1, 10)
    }

    client.publish("env/temperature", json.dumps(temp_data))
    client.publish("env/humidity", json.dumps(humidity_data))
    client.publish("env/air_quality", json.dumps(air_data))
    client.publish("env/Co2", json.dumps(Co2_data))

    print(f"[{datetime.now().isoformat()}] Published:")
    print(f"  Temperature: {temp_data['value']} C")
    print(f"  Humidity: {humidity_data['value']} %")
    print(f"  Air Quality: {air_data['value']} ppm")
    print(f"  CO2: {Co2_data['value']} ppm")
    print("---")
    time.sleep( 5)

    #when you create randomn set of data for testing, you call these set of data mock :)))
    #mqtt : publisher/subsciber/broker (communication protocols) in my project : simulated sensor (publisher), broker(zanzara), py sub 
    #subscriber : does 3 things : connect to broker/subscribe to a topic/reacts when message arrive 
    #we also had to have dictionary with while loop 