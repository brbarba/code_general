import os
import smtplib
import requests

EMAIL_ADDRESS = os.environ['EMAIL_USER']
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
access_token = os.environ.get('WEBEX_TEAMS_TOKEN')
room_ID = os.environ.get('NOTIFY_ROOM_ID')

print(WEBEX_TEAMS_TOKEN)
print(NOTIFY_ROOM_ID)
