import requests
import json

api_key = "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"

response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json={
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "Hello, who are you?"}],
        "max_tokens": 50
    }
)

print(response.status_code)
print(response.json())
