from rest_framework import serializers

from communications.models import Message


class MessageSerializer(serializers.ModelSerializer):
    "Serializer for message"
    sender = serializers.ReadOnlyField(source='sender.username')
    receiver = serializers.ReadOnlyField(source='receiver.username')

    class Meta:
        model = Message
        fields = ('id', 'sender', 'receiver', 'message_text', 'subject', 'creation_date', 'unread')
        read_only_fields = ('id', 'creation_date')
