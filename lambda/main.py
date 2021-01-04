import urllib, urllib3, json, os, string, datetime, requests, googlemaps, sys, base64
from urllib import request, parse

TWILIO_SMS_URL = "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json"
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TO_NUMBER = os.environ.get("TO_NUMBER")
FROM_NUMBER = os.environ.get("FROM_NUMBER")

def lambda_handler(event, context):

    # traffic check
    now = datetime.datetime.now()
    client = googlemaps.Client(key=(os.environ['API_KEY']))
    try:
        directions = client.directions(os.environ['office_address'], os.environ['home_address'], alternatives=True, mode=os.environ['mode'], avoid="ferries", departure_time=now, traffic_model=os.environ['traffic_model'])
        table = {}
        for i in range(len(directions)):
            table.setdefault(directions[i]["summary"])
            table[directions[i]["summary"]] = directions[i]["legs"][0]["duration_in_traffic"]["text"]
        result_list = []
        for key, value in table.items():
            result_list.append(" ".join([key, ":", value, "\n"]))
        message = "".join(result_list)
    except:
        print("Error while executing the function")
        exit(1)

    to_number = TO_NUMBER
    from_number = FROM_NUMBER
    body = message

    if not TWILIO_ACCOUNT_SID:
        return "Unable to access Twilio Account SID."
    elif not TWILIO_AUTH_TOKEN:
        return "Unable to access Twilio Auth Token."
    elif not to_number:
        return "The function needs a 'To' number in the format +12023351493"
    elif not from_number:
        return "The function needs a 'From' number in the format +19732644156"
    elif not body:
        return "The function needs a 'Body' message to send."

    # insert Twilio Account SID into the REST API URL
    populated_url = TWILIO_SMS_URL.format(TWILIO_ACCOUNT_SID)
    post_params = {"To": to_number, "From": from_number, "Body": body}

    # encode the parameters for Python's urllib
    data = parse.urlencode(post_params).encode()
    req = request.Request(populated_url)

    # add authentication header to request based on Account SID + Auth Token
    authentication = "{}:{}".format(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    base64string = base64.b64encode(authentication.encode('utf-8'))
    req.add_header("Authorization", "Basic %s" % base64string.decode('ascii'))

    try:
        # perform HTTP POST request
        with request.urlopen(req, data) as f:
            print("Twilio returned {}".format(str(f.read().decode('utf-8'))))
    except Exception as e:
        # something went wrong!
        return e

    return "SMS sent successfully!"