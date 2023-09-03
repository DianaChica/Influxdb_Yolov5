import time
import subprocess
import os
from datetime import datetime
import database
import glob
import logging

# Basic logging configuration
logging.basicConfig(filename='count_people.log', level=logging.DEBUG)

# Connect to the database
client = database.connect_to_db()

# If the camera is internal, use source 0; otherwise, determine the camera's source
while True:
    # Perform object detection
    subprocess.Popen(['python3', 'detect.py', '--source', 'rtsp://ip:8554/cam', '--weights', 'yolov5s.pt','--save-txt'])

    # Process the output file from 'detect.py' to count the detected people
    # Find the most recent txt file in the output directory
    logging.info("Searching for the most recent txt file...")
    list_of_files = glob.glob('runs/detect/exp*/labels/*.txt')

    if not list_of_files:  # If the list is empty, no people were detected
        count = 0
    else:
        latest_file = max(list_of_files, key=os.path.getctime)

        # Read the txt file
        logging.info("Reading the txt file...")
        with open(latest_file, 'r') as f:
            # Count how many times 'person' appears in the file
            count = sum(1 for line in f if line.startswith('0'))  # '0' is the class index for 'person'

    # Print the count value
    logging.info(f"Detected count: {count}")

    # Add the person count to the database
    timestamp = datetime.now()

    logging.info("Attempting to add the person count to the database...")
    try:
        database.add_person_count(client, count, timestamp)
        logging.info(f"Inserted count of {count} at {datetime.now()}")

    except Exception as e:
        logging.error(f"Error adding person count to the database: {e}")

    # Sleep for 30 seconds before the next iteration
    time.sleep(30)
