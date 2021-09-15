import os

BOT_TOKEN = os.environ.get('People_ready_bot_TOKEN')
Path = os.environ.get('PATH')
print('hola')
print(BOT_TOKEN)
print(Path)

from decouple import config

API_USERNAME = config('USER')
API_KEY = config('KEY')

print(API_USERNAME)
print(API_KEY)
