from pymongo import MongoClient #mongoclient is just a connector betwween py and mongo, exactly like sqlit3
from datetime import datetime

def save_to_mongodb(payload): #come sempre creating a function to save data in mongo db 
    client = MongoClient("mongodb://localhost:27017/")
    db = client["environmental_monitoring"]
    collection = db["air_quality"]
    
    collection.insert_one(payload)
    client.close()
    print(f"Air quality data saved to MongoDB: {payload['value']} {payload['unit']}")

def show_mongodb():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["environmental_monitoring"]
    collection = db["air_quality"]
    
    print("--- Air Quality Data 🪄---")
    for doc in collection.find({}, {"_id": 0}):
        print(doc)
    client.close()

def reset_mongodb():
    client = MongoClient("mongodb://localhost:27017/")
    client.drop_database("environmental_monitoring")
    print("MongoDB reset complete.")
    client.close()