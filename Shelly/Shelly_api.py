import requests
import os

SHELLY_HOME_Token = os.environ.get('SHELLY_TOKEN')
Device_ID = os.environ.get('Alacena_Shelly_id')

url = "https://shelly-3-eu.shelly.cloud/device/relay/control/"

payload={'auth_key': SHELLY_HOME_Token,
'turn': 'on',
'channel': '0',
'id': Device_ID}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
