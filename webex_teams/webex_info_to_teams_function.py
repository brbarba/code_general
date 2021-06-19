import requests
import os
import json
BOT_TOKEN = os.environ.get('People_ready_bot_TOKEN')
userid = input("Enter the userID to check status: ")

url = "https://webexapis.com/v1/people?email=" + userid + "@cisco.com"
#variables to send message
ToEmail = 'brbarba@cisco.com'

apiUrl = 'https://webexapis.com/v1/messages'
access_token = 'replace with your_access_token'
room_ID = 'replace with your room ID'
email_ID = 'gifbot@webex.bot'
httpHeaders = { 'Content-type': 'application/json', 'Authorization': 'Bearer ' + BOT_TOKEN }

payload={}
headers = {
  'Authorization': 'Bearer ' + BOT_TOKEN }

def get_status():
    global name
    global status
    response = requests.request("GET", url, headers=headers, data=payload)
    json_data = json.loads(response.text)
    name = response.json()["items"][0]["displayName"]
    status = response.json()["items"][0]["status"]

def post_message(status_post):
    message = name + ' tiene como status \n' + status_post
    body = { 'toPersonEmail': ToEmail, 'text': message }
    response_post = requests.post( url = apiUrl, json = body, headers = httpHeaders )

#    print('\n')
#    print(message)
#    print( response_post.status_code )

print(url)

get_status()

post_message(status)

#print(BOT_TOKEN)
#print(ToEmail)
#print( response_post1.status_code )
#print( response_post1.text )
