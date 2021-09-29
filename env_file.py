import os
from dotenv import load_dotenv

load_dotenv()

user_na_from_file = os.getenv('USER_NA')
token_from_file = os.getenv('TOKEN')
BOT_TOKEN = os.getenv('People_ready_bot_TOKEN')

print(user_na_from_file)
print(token_from_file)
print(BOT_TOKEN)
