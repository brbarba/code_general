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

print(url)
response = requests.request("GET", url, headers=headers, data=payload)
json_data = json.loads(response.text)
name = response.json()["items"][0]["displayName"]
status = response.json()["items"][0]["status"]
message = name + ' tiene como status ' + status
print('\n')
print(message)

body = { 'toPersonEmail': ToEmail, 'text': 'esta disponible' }

response_post = requests.post( url = apiUrl, json = body, headers = httpHeaders )

#print(BOT_TOKEN)
#print(ToEmail)
print( response_post.status_code )
print( response_post.text )
