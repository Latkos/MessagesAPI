from rest_framework import generics, status, permissions
from django.shortcuts import render
from messager.models import Message
from messager.serializers import MessageSerializer


class MessageList(generics.ListAPIView):
    Message.objects.create(title='title1', content='content1')
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
