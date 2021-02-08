
import requests
import os
# documentation at https://developer.webex.com/docs/api/v1/messages/create-a-message

apiUrl = 'https://webexapis.com/v1/messages'
access_token = os.environ.get('WEBEX_TEAMS_TOKEN')
room_ID = os.environ.get('NOTIFY_ROOM_ID')
email_ID = 'gifbot@webex.bot'


httpHeaders = { 'Content-type': 'application/json', 'Authorization': 'Bearer ' + access_token }

body = { 'roomId': room_ID, 'text': 'Test notification 4\nusando room_ID como variable\nFrom Pyhton' }
#body = { 'toPersonEmail': 'gifbot@webex.bot', 'text': 'Hello' }

response = requests.post( url = apiUrl, json = body, headers = httpHeaders )

print( response.status_code )
print( response.text )

messages = [
    'as an example of markdown',
    '**Warning!!!**',
    '_Warning!!!_',
    '[Danger, Will Robinson!!!](https://en.wikipedia.org/wiki/Lost_in_Space#Catchphrases)'
    ]

for message in messages:

    body = { 'roomId': room_ID, 'markdown': message }
    response = requests.post( url = apiUrl, json = body, headers = httpHeaders )

    print( response.status_code )
    print( response.text )
