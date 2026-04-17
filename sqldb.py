import sqlite3 

def save_to_sqlite(payload:dict): #payload is a dictionary
    conn = sqlite3.connect("sensor_data.db")    #conn represent connection
    cursor = conn.cursor()             #When you open a database connection, you cant directly write to it you need a cursor to execute commands
    cursor.execute("""                                            
        CREATE TABLE IF NOT EXISTS temperature (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value REAL,
            unit TEXT,
            timestamp TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS humidity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value REAL,
            unit TEXT,
            timestamp TEXT
        )
    """)
    
    sensor_type = payload.get("type") #the logic is easy we are saying that where to save the database on the type
    
    if sensor_type == "temperature":
        cursor.execute(
            "INSERT INTO temperature (value, unit, timestamp) VALUES (?, ?, ?)",
            (payload["value"], payload["unit"], payload["timestamp"])
        )
    elif sensor_type == "humidity":
        cursor.execute(
            "INSERT INTO humidity (value, unit, timestamp) VALUES (?, ?, ?)", #used question mark as placeholder 
            (payload["value"], payload["unit"], payload["timestamp"])
        )
    
    conn.commit()
    conn.close() #here 

def show_db():
    conn = sqlite3.connect("sensor_data.db") 
    cursor = conn.cursor() #same as always
    print("--- Temperature ---")
    for row in cursor.execute("SELECT * FROM temperature"):
        print(row) #we * from temrpreture and fetch every row from temp and loop through each row one by one and prints it 
    print("--- Humidity ---")
    for row in cursor.execute("SELECT * FROM humidity"):
        print(row) #the same for humidity 
    conn.close()  #the connection must be closed 

def reset_db():
    conn = sqlite3.connect("sensor_data.db") #first we open a connection through cursor to database 
    cursor = conn.cursor()                   
    cursor.execute("DROP TABLE IF EXISTS temperature") 
    cursor.execute("DROP TABLE IF EXISTS humidity")
    conn.commit()            #safety operation, you can rollback if you dont commit if you commit stai cucinato
    conn.close() #like opening the door doing your stuff and closing
    print("Database reset ⭐")
    
    
    #inside the cursor you can write the sql language 
    #a database cursor is your intermediary agent that does operations inside a database on your behalf  
    #why i have to use dictionary? because dictionary in python acts as a single row in sql thats why we have to use for loop in show_db 


#the data arrives at subscriber
#       ↓
#it's temperature → go to SQLite"
#       ↓
#rrives at SQLite
#       ↓
#it's temperature → go to temperature TABLE"
#       ↓
#     saved! """