from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.response import Response

# Create your views here.
class ChatList(APIView):
    def get(self, request, format=None):
        chats = (Chat.objects
                 .all())
        serializer = ChatSerializer(chats, many=True)
        return(Response(serializer.data))