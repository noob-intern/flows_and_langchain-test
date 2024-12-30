import requests


API_URL = "https://ai.voiceerp.com/api/v1/prediction/75a887db-d000-49d6-bcbe-aa10a143ee1c"


def query(api_url, prompt):
    """
    Sends a single-turn question to the API.
    The prompt should include all previous conversation context if you need it.
    """
    payload = {"question": prompt}
    response = requests.post(api_url, json=payload)
    response.raise_for_status()
    return response.json()


def main():
    conversation_log = ""
    
    # First question
    user_question = "Help me to buy a good phone under 50k bdt?"
    conversation_log += f"User: {user_question}\n"
    
    # Send entire conversation as the "question"
    response_data = query(API_URL, conversation_log)
    assistant_answer = response_data.get("answer", "No answer found.")
    
    conversation_log += f"Assistant: {assistant_answer}\n"
    
    print(f"Assistant: {assistant_answer}\n")
    
    # Ask a follow-up question
    followup_question = "Which brand has the best camera in that price range?"
    conversation_log += f"User: {followup_question}\n"
    
    # Send the entire updated conversation
    response_data = query(API_URL, conversation_log)
    followup_answer = response_data.get("answer", "No answer found.")
    
    conversation_log += f"Assistant: {followup_answer}\n"
    
    print(f"Assistant: {followup_answer}")


if __name__ == "__main__":
    main()