from rest_framework import serializers
from messager.models import Message


# serializing the list requires an url as field, the name message-detail is standard and thus we don't need
# any special view for it
class MessageListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='message-detail')

    class Meta:
        model = Message
        fields = ['title', 'url', 'view_counter']
        read_only_fields = ['view_counter']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['title', 'content', 'view_counter']
        read_only_fields = ['view_counter']
