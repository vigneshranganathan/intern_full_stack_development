from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import QAEntry

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class QuestionForm(forms.ModelForm):
    class Meta:
        model = QAEntry
        fields = ["question_text"]
        widgets = {
            "question_text": forms.Textarea(
                attrs={
                    "rows": 2,
                    "placeholder": "Ask a question about electrical machines..."
                }
            )
        }
