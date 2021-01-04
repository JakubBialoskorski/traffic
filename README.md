# traffic
Check the travel time between two points, using Google Maps API

---
Usage:

* Obtain free Google Maps API key: https://developers.google.com/maps/documentation/javascript/get-api-key
* Run ```pip install -r requirements.txt```
* Copy the program: ```cp traffic.py /usr/local/bin/traffic && chmod +x /usr/local/bin/traffic```
* Run with ```traffic --start "FIRST ADDRESS" --end "SECOND ADDRESS"``` - it will initialize the configuration (only first time usage) and show all possible routes (up to three) with travel times:

![Usage example](/screenshots/screenshot1.png?raw=true)

* You can put optional parameter at the end to change traffic model calculations: ```--model YOUR_CHOICE``` :
1. ```best_guess``` is the default mode used by Google Maps GUI
2. ```optimistic``` will show to best possible time that can be achieved on your route
3. ```pessimistic``` will show the worst possible time (including historical data) for your route

Lambda version can be found [here](/lambda).
