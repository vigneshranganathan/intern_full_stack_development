from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, QuestionForm
from .models import QAEntry
from .chatgpt_helper import get_answer_from_chatgpt
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def dashboard_view(request):
    form = QuestionForm()
    entries = QAEntry.objects.filter(user=request.user).order_by("-created_at")[:50]
    return render(request, "dashboard.html", {"form": form, "entries": entries})

@login_required
def ask_question_ajax(request):
    if request.method == "POST":
        question_text = request.POST.get("question_text", "").strip()
        if not question_text:
            return JsonResponse({"error": "Empty question"}, status=400)
        answer = get_answer_from_chatgpt(question_text)
        entry = QAEntry.objects.create(
            user=request.user,
            question_text=question_text,
            answer_text=answer,
            plugin_source="chatgpt",
        )
        return JsonResponse({
            "question": entry.question_text,
            "answer": entry.answer_text,
        })
    return JsonResponse({"error": "Invalid method"}, status=405)
