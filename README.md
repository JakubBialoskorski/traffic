# traffic
Check the most pessimistic travel time between two points, using Google Maps API.

---
Usage:

* Obtain free Google Maps API key: https://developers.google.com/maps/documentation/javascript/get-api-key
* Installation: ```cp traffic.py /usr/local/bin/traffic & chmod +x /usr/local/bin/traffic```
* Run with ```traffic --token YOUR_API_KEY --start "FIRST ADDRESS" --end "SECOND ADDRESS"``` - it will show all possible routes (up to three) with travel times:

![Usage example](/screenshots/screenshot1.png?raw=true)
