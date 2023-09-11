from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.client.query_api import QueryApi
import logging

def connect_to_db():
    """Connect to the InfluxDB database."""
    client = InfluxDBClient(url="ip:port", "your_token", org="your_org")

    return client

def add_person_count(client, count, timestamp):
    """Add a new person count to the database."""
    write_api = client.write_api(write_options=SYNCHRONOUS)
    p = Point("person_count").field("count", count).time(timestamp)
    try:
        write_api.write("ocupancia", "detect", p)
        logging.info(f"Successfully wrote count of {count} at {timestamp}")

    except Exception as e:
        logging.error(f"Error writing to database: {e}")
