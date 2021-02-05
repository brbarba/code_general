import os
import smtplib
import requests

EMAIL_ADDRESS = os.environ['EMAIL_USER']
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

print(EMAIL_ADDRESS)
print(EMAIL_PASSWORD)
