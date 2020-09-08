import requests
import json
import time
import pprint
import os.path
import datetime

## Get the JSON response from Nest Router
nestresponse = requests.get(
    url="http://192.168.86.1/api/v1/status",
).json()

## Internet Online Check

onlinenest = nestresponse["wan"]["online"]
#print("Internet Online:")
#print(onlinenest)

if onlinenest==True:
 print(onlinenest)
 exit(0)
else:
 print(onlinenest)
 exit(2)

