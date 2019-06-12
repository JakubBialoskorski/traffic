#!/usr/bin/env python

import googlemaps
import requests
import sys
from datetime import datetime

#Enter your Google API Token below
token = 'PUT_YOUR_TOKEN_HERE'

start = sys.argv[1]
end = sys.argv[2]
now = datetime.now()
client = googlemaps.Client(key=token)

#Get directions for driving with most pessimistic travel time
try:
    directions = client.directions(start,end,alternatives=True,mode="driving",avoid="ferries",departure_time=now,traffic_model="pessimistic")

#Prepare data
    table = dict()
    for i in range(len(directions)):
        table.setdefault(directions[i]["summary"])
        table[directions[i]["summary"]] = directions[i]["legs"][0]["duration"]["text"]
    result_list = []
    for key,value in table.items():
        result_list.append(' '.join([key,':',value, "\n"]))

#Prepare the output
    message = ''.join(result_list)
    print message

#Error handling
except:
    error = 'Error during processing'
    print 'Error'
