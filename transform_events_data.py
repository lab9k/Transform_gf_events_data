import json
import requests

# All filtered Gentse feesten events
FilteredEvents = []

# Load json data gentse feesten events
with open('data/gentsefeestenevents.json') as json_data:
    events = json.load(json_data)
    count = 0
    for event in events:
      if event["location"] != None:
        # Count events with location
        count = count + 1
        # API request to get the location for our event
        r = requests.get(event["location"])
        location = r.json()
        # print(location["address"])
        
        # rebuild data structure for event 
        filteredEvent = {}
        filteredEvent["name"] = event["name"]["nl"]
        filteredEvent["address"] = location["address"]["streetAddress"]

        # list of filtered events
        FilteredEvents.append(filteredEvent)

        # TESTING PURPOSES OTHERWISE ALL 5400 EVENTS WILL BE LOOPED
        if count == 2:
          break


    print(count)
    print(FilteredEvents)