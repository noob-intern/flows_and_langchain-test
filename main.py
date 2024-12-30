import requests
import json

url = "https://google.serper.dev/search"

payload = json.dumps({
  "q": "apple inc"
})
headers = {
  'X-API-KEY': 'e85888e24dc81e84f24bf35eca2e1b6f6130605b',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
