from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Chat, Message

# Register the CustomUserAdmin class with the admin site
@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['name', 'createdAt']
    
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['createdBy', 'content', 'createdAt']