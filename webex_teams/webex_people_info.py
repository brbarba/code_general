import requests
import os
import json
BOT_TOKEN = os.environ.get('People_ready_bot_TOKEN')
userid = 'brbarba'
url = "https://webexapis.com/v1/people?email=" + userid + "%40cisco.com"
payload={}
headers = {
  'Authorization': 'Bearer ' + BOT_TOKEN }

print(url)
response = requests.request("GET", url, headers=headers, data=payload)
json_data = json.loads(response.text)
print('\n')
print(response.text)
print('\n')
print(json_data)
print('\n')
print(json_data['displayName'])
