from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Chat

# Register the CustomUserAdmin class with the admin site
@admin.register(Chat)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ['name']