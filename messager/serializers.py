from rest_framework import serializers

from messager.models import Message


class MessageSerializer(serializers.ModelSerializer):
    link_to_content = serializers.HyperlinkedIdentityField(view_name='message-content')

    class Meta:
        model = Message
        fields = ['title', 'link_to_content','view_counter']

