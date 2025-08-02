from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
    path('ask/', views.ask_question_view, name='ask_question'),
    path('question/<int:pk>/', views.question_detail_view, name='question_detail'),
    path('questions/', views.questions_list_view, name='questions_list'),
    path('profile/', views.profile_view, name='profile'),
    path('api/regenerate-answer/<int:pk>/', views.regenerate_answer_view, name='regenerate_answer'),
]