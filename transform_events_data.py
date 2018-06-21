import json
import requests

# All filtered Gentse feesten events
filteredEvents = []

# Load json data gentse feesten events
with open('data/gentsefeestenevents.json') as json_data:
    events = json.load(json_data)
    count = 0
    for event in events:
      if event["location"] != None:
        # API request to get the location for our event
        r = requests.get(event["location"])
        location = r.json()
        
        # build data structure for 1 event 
        filteredEvent = {}

        # Minimum requirements for an event are: address,name,startDate & endDate
        if location["address"] == None or event["name"] == None or event["startDate"] == None or event["endDate"] == None:
          continue
        
        # Count events
        count = count + 1

        filteredEvent["name"] = event["name"]["nl"]
        filteredEvent["startDate"] = event["startDate"]
        filteredEvent["endDate"] = event["endDate"]
        filteredEvent["address"] = location["address"]["streetAddress"]

        # Additional fields (not necesssary to be an event)
        if event["description"] != None: 
          filteredEvent["description"] = event["description"]["nl"]

        if event["image"] != None:
          filteredEvent["image_url"] = event["image"]["thumbnailUrl"]    

        # list of filtered events
        filteredEvents.append(filteredEvent)

        print(count)

        # TESTING PURPOSES: OTHERWISE ALL +-5400 EVENTS WILL BE LOOPED
        """ if count == 30:
          break """


    print("amount of events with location:", count)
    # print(filteredEvents)
    
    # save output as JSON file 
    with open('data/filtered_gf_events.json', 'w') as outfile:
      json.dump(filteredEvents, outfile)