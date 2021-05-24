from django.db.models import F
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response

from messager.models import Message
from messager.serializers import MessageListSerializer, MessageSerializer


class MessageListViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'update':
            return MessageSerializer
        print(self.action)
        return MessageListSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Message.objects.filter(pk=instance.id).update(view_counter=F('view_counter') + 1)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
