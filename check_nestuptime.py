import requests
import json
import time
import pprint
import os.path
import datetime

## Get the JSON response from Nest Router
nestresponse = requests.get(
    url="http://192.168.0.1/api/v1/status",
).json()

## Uptime string analysis

# This is Not human readable so will convert it
#print("System Uptime is:")
#print(nestresponse["system"]["uptime"])

uptimenest = nestresponse["system"]["uptime"]
uptimehuman = str(datetime.timedelta(seconds=uptimenest))

#print("Nest Uptime is:")
print(uptimehuman)

