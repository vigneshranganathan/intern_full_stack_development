# import openai
# from openai import OpenAI
# from django.conf import settings

# openai.api_key = settings.OPENAI_API_KEY
# # client = OpenAI()
# def get_chatgpt_response(question):

#     completion = openai.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Hello!"}
#     ]
#     )

#     return completion.choices[0].message
import google.generativeai as genai
from django.conf import settings

# Configure the Google Generative AI API key
genai.configure(api_key=settings.GEMINI_API_KEY)

def get_google_ai_response(prompt):
    # Define the generation configuration
    generation_config = {
        "temperature": 1,                  # Controls the randomness of the output
        "top_p": 0.95,                     # Cumulative probability for nucleus sampling
        "top_k": 64,                       # Limits the number of tokens considered
        "max_output_tokens": 8192,        # Maximum number of tokens in the output
        "response_mime_type": "text/plain",  # Response format
    }

    # Create an instance of the GenerativeModel
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config
    )

    # Start a chat session
    chat_session = model.start_chat(history=[])

    # Send the message and get the response
    response = chat_session.send_message(prompt)
    
    return response.text

# Example usage
# response_text = get_google_ai_response("Hello!")
# print(response_text)
