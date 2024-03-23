from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.db.models import Max
from rest_framework.response import Response

# Create your views here.

class ChatList(APIView):
    def get(self, request, format=None):
        chats = Chat.objects.annotate(last_message=Max('message__createdAt')).order_by('-last_message')
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)
