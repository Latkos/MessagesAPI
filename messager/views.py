from rest_framework import generics, status, permissions, viewsets
from django.shortcuts import render
from messager.models import Message
from messager.serializers import MessageListSerializer, MessageSerializer


class MessageListViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return MessageListSerializer
        if self.action == 'retrieve':
            return MessageSerializer
        return MessageListSerializer
