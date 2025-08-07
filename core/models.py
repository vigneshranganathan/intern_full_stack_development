from django.db import models
from django.contrib.auth.models import User

class QAEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.TextField()
    answer_text = models.TextField()
    plugin_source = models.CharField(max_length=100, default="chatgpt")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.question_text[:50]}"
