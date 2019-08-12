#!/usr/bin/env python

import googlemaps
import requests
import sys
from pathlib import Path
from datetime import datetime
import argparse

# Check if the config exists - if not, then create it. If yes - read it.
config = Path("config.txt")
if config.is_file():
    f = open("config.txt","r")
    if f.mode == 'r':
        API_KEY = f.read()
    pass
else:
    print "No configuration detected. \n"
    API_KEY = raw_input("Please put/paste your Google Maps API key: ")
    f = open("config.txt", "w+")
    f.write(API_KEY)
    f.close()

parser = argparse.ArgumentParser(description="Check travel time between two points, using Google Maps API")
parser.add_argument("--start", help="Starting point of your journey", required=True)
parser.add_argument("--end", help="Final point of your journey", required=True)
parser.add_argument("--model", help="(optional) best_guess (default) / optimistic / pessimistic", required=False)
args = parser.parse_args()

now = datetime.now()
client = googlemaps.Client(key=API_KEY)

# Get directions for driving with most pessimistic travel time
try:
    directions = client.directions(args.start, args.end, alternatives=True, mode="driving", avoid="ferries", departure_time=now, traffic_model=args.model)

    # Prepare data
    table = {}
    for i in range(len(directions)):
        table.setdefault(directions[i]["summary"])
        table[directions[i]["summary"]] = directions[i]["legs"][0]["duration_in_traffic"]["text"]
    result_list = []
    for key, value in table.items():
        result_list.append(" ".join([key, ":", value, "\n"]))

    # Prepare the output
    message = "".join(result_list)
    print(message)

# Error handling
except:
    print("Error during processing")
    exit(1)
