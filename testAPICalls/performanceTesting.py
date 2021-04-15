import requests
import json
import random
import time

url = "https://registration.eutops.at/api/v1/garminDailySummaries"

with open('dailiesTemplate.json') as f:
  data = json.load(f)

headers = {
  'Content-Type': 'application/json'
}

totalTime = 0
totalNumbers = 1

for count in range(1000000):
    jsonPayload = {
        "dailies": []
    }
    y = random.randint(1, 100)
    for items in range(y):
        totalNumbers = totalNumbers + items
        with open('dailiesTemplate.json') as f:
            newdataitem = json.load(f)
        newdataitem["summaryId"] = newdataitem["summaryId"] + "-" + str(count) + "-" + str(items)
        jsonPayload["dailies"].append(newdataitem)
    #print(jsonPayload)
    start = time.time()
    response = requests.request("POST", url, headers=headers, data=json.dumps(jsonPayload))
    end = time.time()
    print("####################")
    totalTime = totalTime + end - start
    print("Items " + str(y) + ": " + str(end - start))
    print(response.text)

print("==================================")
print("avarage time: " + str(totalTime/totalNumbers))