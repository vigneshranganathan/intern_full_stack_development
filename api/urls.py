from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login,name="login"),
    path('register/', views.register,name="register"),
    path('chat/', views.chat,name="chat"),
    path('get_messages/', views.get_messages,name="get_chat"),
    path('add_session/', views.add_session,name="add_session"),
    path('get_sessions/', views.get_sessions,name="get_sessions"),

]