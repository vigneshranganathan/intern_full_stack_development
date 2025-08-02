from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now

class Question(models.Model):
    CATEGORY_CHOICES = [
        ('DC_MOTORS', 'DC Motors'),
        ('AC_MOTORS', 'AC Motors'),
        ('TRANSFORMERS', 'Transformers'),
        ('GENERATORS', 'Generators'),
        ('CONTROL_SYSTEMS', 'Control Systems'),
        ('POWER_ELECTRONICS', 'Power Electronics'),
        ('OTHER', 'Other'),
    ]
    
    title = models.CharField(max_length=200, help_text="Brief title for your question")
    content = models.TextField(help_text="Detailed description of your question")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHER')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('question_detail', kwargs={'pk': self.pk})

class Answer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='answer')
    content = models.TextField()
    source = models.CharField(max_length=50, default='ChatGPT')
    confidence_score = models.FloatField(default=0.0, help_text="AI confidence in the answer")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Answer to: {self.question.title}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    expertise_level = models.CharField(
        max_length=20,
        choices=[
            ('BEGINNER', 'Beginner'),
            ('INTERMEDIATE', 'Intermediate'),
            ('ADVANCED', 'Advanced'),
            ('EXPERT', 'Expert'),
        ],
        default='BEGINNER'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

class QuestionView(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='views')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ip_address = models.GenericIPAddressField()
    viewed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['question', 'user', 'ip_address']