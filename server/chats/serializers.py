from rest_framework import serializers

from .models import Chat, Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'createdAt',
            'content'
        ]

class ChatSerializer(serializers.ModelSerializer):
    lastMessage = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        fields = [
            "id",
            "name",
            "createdAt",
            "createdBy",
            "lastMessage",
        ]

    def get_lastMessage(self, obj):
        lastMessage = Message.objects.filter(chatID=obj).order_by('-createdAt').first()
        if lastMessage:
            return MessageSerializer(lastMessage).data
        return None