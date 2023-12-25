from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from communications.models import Message

User = get_user_model()


class MessageSerializer(serializers.ModelSerializer):
    "Serializer for message"
    sender = serializers.ReadOnlyField(source='sender.username')
    receiver = serializers.CharField(source='receiver.username')

    class Meta:
        model = Message
        fields = ('id', 'sender', 'receiver', 'message_text', 'subject', 'creation_date', 'unread')
        read_only_fields = ('id', 'creation_date', 'unread')

    def create(self, validated_data):
        receiver_username = validated_data.get('receiver')
        if receiver_username:
            receiver = get_object_or_404(User, username=receiver_username.get('username'))
            validated_data['receiver'] = receiver
        message = Message.objects.create(**validated_data)
        return message
