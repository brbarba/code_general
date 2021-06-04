import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/"
querystring = {"deck_count": "6"}

payload={}
headers = {
  'Cookie': '__cfduid=df097fb749668270b7f41dcd8381ee6991611630570'
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

deck = response.json()
deck_id = deck['deck_id']
print(deck_id)
