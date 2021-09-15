import requests
import os
from rich import print

BOT_TOKEN = os.environ.get('People_ready_bot_TOKEN')
ToEmail = 'brbarba@cisco.com'
mensa = "**Title:**"

apiUrl = 'https://webexapis.com/v1/messages'
access_token = 'replace with your_access_token'
room_ID = 'replace with your room ID'
email_ID = 'gifbot@webex.bot'
httpHeaders = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + BOT_TOKEN}

# body = { 'roomId': room_ID, 'text': 'Test notification 4\nusando room_ID como variable\nFrom Pyhton' }
body = { 'toPersonEmail': ToEmail, 'text': mensa }

response = requests.post(url=apiUrl, json=body, headers=httpHeaders)

print(response.status_code)
print(response.text)
