from django.db.models import F
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from messager.models import Message
from messager.serializers import MessageListSerializer, MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['retrieve', 'update', 'create']: # the 2 serializers differ since in list there's url field
            # and in message detail there's content field instead
            return MessageSerializer
        print(self.action)
        return MessageListSerializer

    def retrieve(self, request, *args, **kwargs): # overloaded to be able update the view counter
        instance = self.get_object()
        Message.objects.filter(pk=instance.id).update(view_counter=F('view_counter') + 1)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
