import requests
import os
BOT_TOKEN = os.environ.get('People_ready_bot_TOKEN')
userid = brbarba
url = "https://webexapis.com/v1/people" + userid + "%40cisco.com"
payload={}
headers = {
  'Authorization': 'Bearer ' + BOT_TOKEN }

#response = requests.request("GET", url, headers=headers, data=payload)
print(url)
#print(response.text)
