from decouple import config
import openai

client = openai.OpenAI(api_key=config("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "What is a synchronous motor?"}]
)

print(response.choices[0].message.content)
