import os

EMAIL_ADDRESS = os.environ['EMAIL_USER']
EMAIL_PASSWORD = os.environ['EMAIL_PASS']
access_token = os.environ['WEBEX_TEAMS_TOKEN']
room_ID = os.environ.get('NOTIFY_ROOM_ID')
bot_token = os.environ['CHTRPM_NOTI_BOT_TOKEN']

print(EMAIL_ADDRESS)
print(EMAIL_PASSWORD)
print(access_token)
print(room_ID)
print(bot_token)
