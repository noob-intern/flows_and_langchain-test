import requests

try:
    response = requests.post("https://ai.voiceerp.com/api/v1/prediction/75a887db-d000-49d6-bcbe-aa10a143ee1c", 
                             json={"question": "Help me to buy a good phone under 50k bdt?"})
    response.raise_for_status()
    print(response.json())
except requests.exceptions.HTTPError as http_err:
    print("HTTP error:", http_err)
    # Print more info for debugging:
    print("Response Status Code:", response.status_code)
    print("Response Text:", response.text)
except Exception as e:
    print("An error occurred:", e)