#!/usr/bin/env python

import urllib
import json
import os
import time

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    ######## YAHOOOOO WEATHER
    if req.get("result").get("action") == "yahooWeatherForecast":
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = makeYqlQuery(req)
        if yql_query is None:
            return {}
        yql_url = baseurl + urllib.urlencode({'q': yql_query}) + "&format=json"
        result = urllib.urlopen(yql_url).read()
        data = json.loads(result)
        res = makeWebhookResultWeather(data)
        return res
    elif req.get("result").get("action") == "test1":
        return {
        "speech": "1",
        "displayText": "asdf",
        # "data": data,
        # "contextOut": [],
        "source": "MH8-Hackbot"
        }
    elif req.get("result").get("action") == "busRoutes":
        baseurl = "http://ddot-beta.herokuapp.com/api/api/where/schedule-for-stop/DDOT_"
        apiKey = ".json?key=MHACKS8"
        bus_url = baseurl + req.get("result").get("parameters").get("stop-id") + apiKey
        result = urllib.urlopen(bus_url).read()
        datum = json.loads(result)
        res = makeWebhookResultBus(datum)
        return res

def makeWebhookResultBus(datum):
    print ("-----------------------------1--------------")
    data = datum.get("data")
    if data is None:
        return {}
    print ("-----------------------------2--------------")
    # references = data.get("references")
    # if references is None:
    #     return {}
    #
    # stops = json.loads("stops")
    # if stops is None:
    #     return {}
    # print ("stops")
    # printt (json.dumps(stops, indent=4))
    #
    # name = json.loads(stops[0])["name"]
    # if name is None:
    #     return {}
    # print ("Name: ")
    # print (name)

    entry = data.get('entry')
    if entry is None:
        return {}
    print ("asdffff-----------------------------------")
    stopRouteSchedules = entry.get('stopRouteSchedules')
    if stopRouteSchedules is None:
        return{}
    print ("---------------------------rrrrrrrrrrrrre")
    stopRouteDirectionSchedules = stopRouteSchedules[0]
    print ("--------------FIRST BREAK POINT---------------")
    thing = stopRouteDirectionSchedules[0]
    print (thing)
    print ("--------------BREAK POINT 1.5-----------------")
    scheduleStopTimes = thing["scheduleStopTimes"]
    serviceId = scheduleStopTimes[0]["serviceId"]
    print ("-------------SECOND BREAK POINT----------------")
    # if scheduleStopTimes is None:
    #     return{}
    #
    # serviceId = scheduleStopTimes[0].get('serviceId')
    # if serviceId is None:
    #     return{}
    #
    # arrivalTime = scheduleStopTimes[0].get('arrivalTime')
    # if arrivalTime is None:
    #     return{}
    # newTime = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(arrivalTime/1000))
    # print(json.dumps(serviceId, indent=4))
    #
    # speech = "Next bus is " + serviceId + " and it arrives at " + newtime

    return {
        "speech": serviceId,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "MH8-Hackbot"
    }
#########################################
##        YAHOO API FORMATTING
#########################################
def makeYqlQuery(req):
    result = req.get("result")
    parameters = result.get("parameters")
    city = parameters.get("geo-city")
    if city is None:
        return None

    return "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='" + city + "')"


def makeWebhookResultWeather(data):
    query = data.get('query')
    if query is None:
        return {}

    result = query.get('results')
    if result is None:
        return {}

    channel = result.get('channel')
    if channel is None:
        return {}

    item = channel.get('item')
    location = channel.get('location')
    units = channel.get('units')
    if (location is None) or (item is None) or (units is None):
        return {}

    condition = item.get('condition')
    if condition is None:
        return {}

    # print(json.dumps(item, indent=4))

    speech = "Today in " + location.get('city') + ": " + condition.get('text') + \
             ", the temperature is " + condition.get('temp') + " " + units.get('temperature')
    # speech = "literally troll"
    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "MH8-Hackbot"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=False, port=port, host='0.0.0.0')
