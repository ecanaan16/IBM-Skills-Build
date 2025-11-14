import requests
from dotenv import load_dotenv
import os

#get env contents
load_dotenv()

#API_KEY = os.getenv("WATSONX_API_KEY")
IAM_TOKEN = os.getenv("IAM_ACCESS_TOKEN")
PROJECT_ID = os.getenv("PROJECT_ID")

url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2024-05-01"


#header: who i am and how i am sending data
#payload: actual data i wanna send
#limited to 40 tokens

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {IAM_TOKEN}",
}

payload = {
    "model_id": "ibm/granite-3-8b-instruct",
    "input": "Say hello in Spanish.",
    "parameters": { "max_new_tokens": 40 },
    "project_id": PROJECT_ID
}

#json is universal langauge of API
response = requests.post(url, headers=headers, json=payload)

print(response.json())








