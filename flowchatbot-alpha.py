import requests


API_URL = "https://ai.voiceerp.com/api/v1/prediction/75a887db-d000-49d6-bcbe-aa10a143ee1c"


def main():

    question = "Help me to buy a good phone under 50k bdt?"
    payload = {"question": question}
    
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        print(f"AI Response: {data}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except ValueError:
        print("Received non-JSON response from the API.")


if __name__ == "__main__":
    main()