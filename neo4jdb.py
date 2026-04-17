from neo4j import GraphDatabase
from datetime import datetime

uri = "bolt://localhost:7687"
user = "neo4j"
password = "nooshin7693"  

driver = GraphDatabase.driver(uri, auth=(user, password))

def save_to_neo4j(payload):
    try:
        with driver.session() as session:
            session.execute_write(_create_sensor_and_reading, payload)
        print(f"CO2 data saved to Neo4j: {payload['value']} {payload['unit']}")
    except Exception as e:
        print(f"Error saving to Neo4j: {e}")

def _create_sensor_and_reading(tx, payload):
    sensor_id = int(payload.get("sensor_id"))
    value = payload["value"]
    unit = payload["unit"]
    timestamp = payload["timestamp"]

    tx.run("""
        MERGE (s:Sensor {id: $sensor_id})
        ON CREATE SET s.type = "CO2"
        
        CREATE (r:Reading {
            value: $value,
            unit: $unit,
            timestamp: $timestamp
        })
        
        MERGE (s)-[:REPORTED]->(r)
    """,
    sensor_id=sensor_id,
    value=value,
    unit=unit,
    timestamp=timestamp
    )

def reset_neo4j():
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")
    print("Neo4j reset complete.")