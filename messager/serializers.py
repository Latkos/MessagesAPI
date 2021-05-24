from rest_framework import serializers

from messager.models import Message


class MessageListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='message-detail')

    class Meta:
        model = Message
        fields = ['title', 'url','view_counter']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['title', 'content', 'view_counter']