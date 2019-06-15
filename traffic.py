#!/usr/bin/env python

import googlemaps
import requests
import sys
from datetime import datetime
import argparse

parser = argparse.ArgumentParser(
    description="Check the most pessimistic travel time between two points, using Google Maps API")
parser.add_argument("--start", help="Starting point of your journey", required=True)
parser.add_argument("--end", help="Final point of your journey", required=True)
args = parser.parse_args()

now = datetime.now()
client = googlemaps.Client(key="YOUR_GOOGLE_MAPS_API_TOKEN_HERE")

# Get directions for driving with most pessimistic travel time
try:
    directions = client.directions(args.start, args.end, alternatives=True, mode="driving", avoid="ferries",
                                   departure_time=now,
                                   traffic_model="pessimistic")

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
