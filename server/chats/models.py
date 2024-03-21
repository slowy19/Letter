from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    createdAt = models.DateTimeField(auto_now_add = True)
    createdBy = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)

    content = models.TextField(blank = True, null = True)
    watchedAt = models.DateTimeField(blank = True, null = True)
    
    
class Chat(models.Model):
    createdAt = models.DateTimeField(auto_now_add = True)
    createdBy = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
    
    messageId = models.ForeignKey(Message, on_delete = models.CASCADE)
