from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets

from communications.models import Message
from .filters import MessageFilter
from .serializers import MessageSerializer


class MessageViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin,
                     mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """Messages viewset"""

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MessageFilter

    def get_queryset(self):
        """redefine  and filter queryset for current logged user"""
        user = self.request.user
        return Message.objects.filter(Q(sender=user) | Q(receiver=user))

    def retrieve(self, request, *args, **kwargs):
        """redefine retrive for reading message"""
        message = get_object_or_404(Message, pk=kwargs.get('pk'))
        if message.receiver == self.request.user:  # only receiver can change message status
            message.unread = False
            message.save()
        return super().retrieve(request, *args, **kwargs)

    def perform_create(self, serializer):
        """redefine create for current logged user"""
        serializer.save(sender=self.request.user)
