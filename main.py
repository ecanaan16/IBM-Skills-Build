import requests
from dotenv import load_dotenv
import os
from pathlib import Path

#get env contents
load_dotenv()

#API_KEY = os.getenv("WATSONX_API_KEY")
WATSONX_API_KEY = os.getenv("WATSONX_API_KEY")

#request iam access token due to hourly reset
def get_iam_token(api_key=WATSONX_API_KEY):
    url = "https://iam.cloud.ibm.com/identity/token"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": api_key
    }

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    token_data = response.json()

    return token_data["access_token"]

IAM_TOKEN = get_iam_token()

#IAM_TOKEN = os.getenv("IAM_ACCESS_TOKEN")
PROJECT_ID = os.getenv("PROJECT_ID")

url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2024-05-01"
MODEL_ID = "ibm/granite-3-8b-instruct"  # matches your working request
BENEFITS_PATH = Path("data/benefits.txt")

#verfication process
if not IAM_TOKEN:
    raise ValueError("IAM_ACCESS_TOKEN missing from .env")
if not PROJECT_ID:
    raise ValueError("PROJECT_ID missing from .env")


#header: who i am and how i am sending data
#payload: actual data i wanna send
#limited to 40 tokens

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {IAM_TOKEN}",
}

payload = {
    "model_id": MODEL_ID,
    "input": "Say hello in Spanish.",
    "parameters": { "max_new_tokens": 40 },
    "project_id": PROJECT_ID
}

#json is universal langauge of API
response = requests.post(url, headers=headers, json=payload)
print(response.json())

def main():
    print("=== Healthcare Benefits Q&A Assistant ===")
    print("Ask me anything about your health plan!")
    print("Type 'quit' to exit.\n")

    while True:
        q = input("You: ")
        if q.lower().strip() in ("quit", "exit"):
            print("Goodbye!")
            break

        answer = answer_benefits_question(q)
        print("\nAssistant:", answer, "\n")


if __name__ == "__main__":
    main()



