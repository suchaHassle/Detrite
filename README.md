# Weather and Bus Info Facebook Messaging Bot With API.AI.

This is a webhook implementation that gets Api.ai classification JSON (i.e. a JSON output of Api.ai /query endpoint) and returns a fulfillment response.

More info about Api.ai webhooks could be found here:
[Api.ai Webhook](https://docs.api.ai/docs/webhook)

# Deploy to:
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

# What does the service do?
It's a weather information fulfillment service that uses [Yahoo! Weather API](https://developer.yahoo.com/weather/).
The services takes the `geo-city` parameter from the action, performes geolocation for the city and requests weather information from Yahoo! Weather public API. Additionally, it offers real-time responses to inquiries for bus stop schedules pulled from the official Detroit Department of Travel transit API. Taking in the bus stop number as parameter, it returns the bus stop name, next bus to arrive and its arrival time.

The service packs the result in the Heroku hosted, Api.ai webhook-compatible response JSON and returns it to Api.ai.
