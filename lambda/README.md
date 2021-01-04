# traffic lambda

* ```pip3 install datetime requests googlemaps -t .```
* ```zip -r9 ~/package.zip *```
* upload it to AWS as .zip
* set environment variables
    * `API_KEY` is your Google Maps API key
    * `FROM_NUMBER` is your Twilio number, taken from the dashboard
    * `TO_NUMBER` is your mobile phone with the country code
    * `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` can be obtained from the Twilio console
    * `home_address` is your own address
    * `office_address` is your work address
    * `traffic_model` should be set to `best_guess` as default
    * `mode` should be set to `driving`
* setup `main.lambda_handler` as handler
* (optional) set CloudWatch rate with CRON, ex. to run it every MON-FRI at 16:30 GMT: `cron(30 16 ? * MON-FRI *)`