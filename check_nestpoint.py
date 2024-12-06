import requests
import json
import time
import pprint
import os.path
import datetime
import sys

# Construct the URL
ip1 = sys.argv[1]
#ip1 = "192.168.0.29"

url1 = "http://%s/api/v1/status" % (ip1)

#print(url1)

## Get the JSON response from Nest Router
nestresponse = requests.get(url1).json()

## Uptime string analysis

# This is Not human readable so will convert it
#print("System Uptime is:")
#print(nestresponse["system"]["uptime"])

uptimenest = nestresponse["system"]["uptime"]
uptimehuman = str(datetime.timedelta(seconds=uptimenest))

#print("Nest Uptime is:")
print(uptimehuman)

