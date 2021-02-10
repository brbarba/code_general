
import requests
import os
# documentation at https://developer.webex.com/docs/api/v1/messages/create-a-message

apiUrl = 'https://webexapis.com/v1/messages'
access_token = os.environ['WEBEX_TEAMS_TOKEN']
room_ID = os.environ['NOTIFY_ROOM_ID']
bot_token = os.environ['CHTRPM_NOTI_BOT_TOKEN']
email_ID = 'cguadarr@cisco.com'


httpHeaders = { 'Content-type': 'application/json', 'Authorization': 'Bearer ' + access_token }

#body = { 'roomId': room_ID, 'text': 'Que oinda\nando haciendo una prueba \nde un  Bot a ver si jala' }
body = { 'toPersonEmail': email_ID, 'text': 'Que oinda\nando haciendo una prueba \nde un  Bot a ver si jala' }

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
