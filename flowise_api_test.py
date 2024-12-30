import requests

API_URL = "https://ai.voiceerp.com/api/v1/prediction/75a887db-d000-49d6-bcbe-aa10a143ee1c"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()
    
output = query({
    "question": "Help me to buy a good phone under 50k bdt?",
})

