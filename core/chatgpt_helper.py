# import os
# from openai import OpenAI

# def get_answer_from_chatgpt(question):
#     client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#     try:
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are an assistant that answers questions about electrical machines."},
#                 {"role": "user", "content": question}
#             ]
#         )
#         answer = response.choices[0].message.content
#         return answer.strip()
#     except Exception as e:
#         return f"Error: {str(e)}"


import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Make sure environment variables are loaded

def get_answer_from_chatgpt(question):
    api_key = os.getenv("GROQ_API_KEY")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-8b-8192",  # Groq's LLaMA 3 model
        "messages": [
            {"role": "system", "content": "You are an assistant that answers questions about electrical machines."},
            {"role": "user", "content": question}
        ]
    }

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=data
        )
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"
