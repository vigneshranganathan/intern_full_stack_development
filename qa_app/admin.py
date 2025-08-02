from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Question, Answer, UserProfile, QuestionView

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'created_at', 'has_answer']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'content']
    readonly_fields = ['created_at']
    
    def has_answer(self, obj):
        return hasattr(obj, 'answer')
    has_answer.boolean = True
    has_answer.short_description = 'Answered'

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'source', 'confidence_score', 'created_at']
    list_filter = ['source', 'created_at']
    search_fields = ['question__title', 'content']
    readonly_fields = ['created_at']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'expertise_level', 'created_at']
    list_filter = ['expertise_level', 'created_at']
    search_fields = ['user__username', 'user__email']

@admin.register(QuestionView)
class QuestionViewAdmin(admin.ModelAdmin):
    list_display = ['question', 'user', 'ip_address', 'viewed_at']
    list_filter = ['viewed_at']
    readonly_fields = ['viewed_at']