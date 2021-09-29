import requests
import os
#from dotenv import load_dotenv

BOT_TOKEN = os.getenv('People_ready_bot_TOKEN')
ToEmail = 'brbarba@cisco.com'

apiUrl = 'https://webexapis.com/v1/messages'
access_token = 'replace with your_access_token'
room_ID = 'replace with your room ID'
email_ID = 'gifbot@webex.bot'
httpHeaders = { 'Content-type': 'application/json', 'Authorization': 'Bearer ' + BOT_TOKEN }

def post_message():
    message = 'La VM de linux Centos8 esta iniciando\nverificar posible power outage'
    body = { 'toPersonEmail': ToEmail, 'text': message }
    response_post = requests.post( url = apiUrl, json = body, headers = httpHeaders )

post_message()


