from django.contrib import admin
from django.urls import path, include
from chats import views

urlpatterns = [
    path('chat-list/', views.ChatList.as_view()),
]