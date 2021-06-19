import requests
import os
import json
BOT_TOKEN = os.environ.get('People_ready_bot_TOKEN')
userid = input("Enter the userID to check status: ")
url = "https://webexapis.com/v1/people?email=" + userid + "@cisco.com"
payload={}
headers = {
  'Authorization': 'Bearer ' + BOT_TOKEN }

print(url)
response = requests.request("GET", url, headers=headers, data=payload)
json_data = json.loads(response.text)
name = response.json()["items"][0]["displayName"]
status = response.json()["items"][0]["status"]
message = name + ' tiene como status ' + status
print('\n')
#print(response.text)
print('\n')
#print(json.dumps(json_data, indent = 4, sort_keys=True))
print('\n')
print(name + ' tiene como status ' + status)
