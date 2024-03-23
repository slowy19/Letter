from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser

class Message(models.Model):
    createdAt = models.DateTimeField(auto_now_add = True)
    createdBy = models.ForeignKey(CustomUser, null = True, on_delete = models.SET_NULL)
    content = models.TextField(blank = True, null = True)
    chatID = models.ForeignKey('Chat', on_delete = models.CASCADE)
    
class Viewed(models.Model):
    messageID = models.ForeignKey('Message', on_delete = models.CASCADE)
    userID = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    watchedAt = models.DateTimeField(auto_now_add = True)
    
class Chat(models.Model):
    name = models.TextField(default = '')
    createdAt = models.DateTimeField(auto_now_add = True)
    createdBy = models.ForeignKey(CustomUser, null = True, on_delete = models.SET_NULL)
    messageId = models.ForeignKey(Message, on_delete = models.CASCADE)
    
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.createdBy.username + "'s chat"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class ChatUsers(models.Model):
    chatID = models.ForeignKey('Chat', null = True, on_delete = models.CASCADE)
    userID = models.ForeignKey(CustomUser, null = True, on_delete = models.CASCADE)