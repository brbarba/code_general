import requests
import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('People_ready_bot_TOKEN')
#BOT_TOKEN = 'MmFjY2EwM2UtYzc0MS00MzI3LThlZTUtN2M5Zjk3MzQ4OWM3ODYzNTFmYjEtZmM5_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
ToEmail = 'brbarba@cisco.com'

proxies = {'https': 'https://proxy.esl.cisco.com:80'}
apiUrl = 'https://webexapis.com/v1/messages'
access_token = 'replace with your_access_token'
room_ID = 'replace with your room ID'
email_ID = 'gifbot@webex.bot'
httpHeaders = { 'Content-type': 'application/json', 'Authorization': 'Bearer ' + BOT_TOKEN }

#body = { 'roomId': room_ID, 'text': 'Test notification 4\nusando room_ID como variable\nFrom Pyhton' }
body = { 'toPersonEmail': ToEmail, 'text': 'working with proxy' }

response = requests.post( url = apiUrl,  proxies = proxies, json = body, headers = httpHeaders )

#print(BOT_TOKEN)
#print(ToEmail)
print( response.status_code )
print( response.text )

messages = [
    'as an example of markdown',
    '**Warning!!!**',
    '_Warning!!!_',
    '[Danger, Will Robinson!!!](https://en.wikipedia.org/wiki/Lost_in_Space#Catchphrases)'
    ]
