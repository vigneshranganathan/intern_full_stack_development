import openai
from openai import OpenAI
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY
# client = OpenAI()
openai.api_key="sk-MRnR23mpDW-XuRrOiuOSx9XORjmV2Zzm80T3br6jGDT3BlbkFJp5_msiAO0KLPvP_p5DTkbaI2zzQRq46glZFkV511QA"
def get_chatgpt_response(question):

    completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
    )

    return completion.choices[0].message
