import requests
import json

url = "https://imdb-api.com/en/API/Title/k_7qzczhez/tt0120737"


payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

with open('test.json', 'w') as file:
    json.dump(response.json(), file, indent=4)

print(response.text.encode('utf8'))
