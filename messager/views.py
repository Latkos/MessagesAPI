from django.db.models import F
from rest_framework import viewsets
from rest_framework.response import Response

from messager.models import Message
from messager.serializers import MessageListSerializer, MessageSerializer


class MessageListViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return MessageSerializer
        return MessageListSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Message.objects.filter(pk=instance.id).update(view_counter=F('view_counter') + 1)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
