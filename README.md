![alt tag](http://i.imgur.com/ULwXmPA.gifv)

# Weather and Bus Info Facebook Messaging Bot With API.AI.

This is a webhook implementation that gets Api.ai classification JSON (i.e. a JSON output of Api.ai /query endpoint) and returns a fulfillment response.


# Deploy to:
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

# What does the service do?
It's a scalable information fulfillment service that uses both local and public API's to provide a central hub for residents of Detroit to easily access updates on the go.
The services takes inputs from Facebook Messenger and runs it through native and customized scripts on API.AI to provide dynamic responses tailor to suit your inquiries.

# Features
Up to date weather at any location through Facebook for the city and requests weather information from the [Yahoo! Weather API](https://developer.yahoo.com/weather/). Additionally, it offers real-time responses answers for bus stop schedules pulled from the official Detroit Department of Travel transit API. Taking in the bus stop number as parameter, it returns the bus stop name, next bus to arrive and its arrival time.

The service is Heroku and Github hosted with webhook-compatible response to JSON.
