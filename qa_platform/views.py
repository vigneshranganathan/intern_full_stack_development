# qa_platform/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import requests
import json
import time
import os

from .models import Question

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                # Log the user out immediately after registration to force them to log in
                # with their new credentials, a best practice for security.
                logout(request)
                messages.success(request, 'Registration successful! Please log in.')
                print(f"User {user.username} successfully registered. Redirecting to login.")
                return redirect('login')
            except Exception as e:
                print(f"Error saving user: {e}")
                messages.error(request, 'An error occurred during registration. Please try again.')
                return render(request, 'registration/register.html', {'form': form})
        else:
            print("Form validation failed. Errors:", form.errors)
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def get_api_key():
    """
    Retrieves the API key from environment variables.
    In a production environment, this is a secure way to manage secrets.
    """
    return os.environ.get("GEMINI_API_KEY", "")


def call_llm_api(prompt, retries=5):
    """
    Calls the Gemini API to generate a response.
    Implements exponential backoff for retries.
    """
    api_key = get_api_key()
    if not api_key:
        return "API key not found. Please set the GEMINI_API_KEY environment variable."

    api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key={api_key}"
    
    headers = {
        "Content-Type": "application/json"
    }

    # We modify the prompt to explicitly instruct the AI to only answer questions about electrical machines.
    # We also ask it to respond with a specific message for off-topic questions.
    full_prompt = (
        "You are a helpful assistant specialized in electrical machines. "
        "Your task is to answer user queries about electrical machines. "
        "If a query is not about electrical machines, you MUST respond with "
        "'I can only answer questions about electrical machines. Please try a different query.' "
        "Do not provide any other information for off-topic questions."
        f"\n\nUser query: {prompt}"
    )
    
    # The payload structure for the Gemini API
    chat_history = []
    chat_history.append({"role": "user", "parts": [{"text": full_prompt}]})
    payload = {"contents": chat_history}
    
    for i in range(retries):
        try:
            response = requests.post(api_url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            
            result = response.json()
            # The response structure is different, we need to parse it accordingly
            if result.get("candidates") and len(result["candidates"]) > 0 and result["candidates"][0].get("content") and result["candidates"][0]["content"].get("parts"):
                text = result["candidates"][0]["content"]["parts"][0].get("text", "No answer found.")
                return text
            else:
                return "No answer found."

        except requests.exceptions.RequestException as e:
            print(f"API call failed: {e}")
            if i < retries - 1:
                sleep_time = 2 ** i
                print(f"Retrying in {sleep_time} seconds...")
                time.sleep(sleep_time)
            else:
                return "An error occurred while fetching the answer from the API."


@login_required
def home(request):
    if request.method == 'POST':
        # Handle the AJAX POST request
        try:
            body = json.loads(request.body)
            question_text = body.get('question_text')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
            
        answer_text = call_llm_api(question_text)

        question = Question.objects.create(
            user=request.user,
            question_text=question_text,
            answer_text=answer_text,
            is_answered=True
        )

        # Return a JSON response instead of a redirect
        return JsonResponse({
            'success': True,
            'question_text': question.question_text,
            'answer_text': question.answer_text,
            'created_at': question.created_at.isoformat()
        })

    questions = Question.objects.filter(user=request.user).order_by('-created_at')

    context = {
        'questions': questions,
    }
    return render(request, 'home.html', context)
