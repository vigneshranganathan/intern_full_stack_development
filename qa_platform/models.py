from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    answer_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_answered = models.BooleanField(default=False)

    def __str__(self):
        """
        String representation of the Question object.
        This is useful for display in the Django Admin.
        """
        return f"Question by {self.user.username}: {self.question_text[:50]}..."
