import requests
import os

BOT_TOKEN = os.environ.get('WEBEX_TEAMS_TOKEN')
ToEmail = 'brbarba@cisco.com'

apiUrl = 'https://webexapis.com/v1/messages'
access_token = 'replace with your_access_token'
room_ID = 'replace with your room ID'
email_ID = 'gifbot@webex.bot'
httpHeaders = { 'Content-type': 'application/json', 'Authorization': 'Bearer ' + BOT_TOKEN }

#body = { 'roomId': room_ID, 'text': 'Test notification 4\nusando room_ID como variable\nFrom Pyhton' }
body = { 'toPersonEmail': ToEmail, 'text': 'From Python' }

response = requests.post( url = apiUrl, json = body, headers = httpHeaders )

print(BOT_TOKEN)
print(ToEmail)
print( response.status_code )
print( response.text )

messages = [
    'as an example of markdown',
    '**Warning!!!**',
    '_Warning!!!_',
    '[Danger, Will Robinson!!!](https://en.wikipedia.org/wiki/Lost_in_Space#Catchphrases)'
    ]

#for message in messages:

#    body = { 'roomId': room_ID, 'markdown': message }
#    response = requests.post( url = apiUrl, json = body, headers = httpHeaders )

#    print( response.status_code )
#    print( response.text )
