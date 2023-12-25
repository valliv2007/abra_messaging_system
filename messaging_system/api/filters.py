from django_filters.rest_framework import FilterSet, filters
from communications.models import Message


class MessageFilter(FilterSet):
    """Filter for messages"""
    receiver = filters.CharFilter(field_name='receiver__username', lookup_expr='icontains')

    class Meta:
        model = Message
        fields = ('unread', 'receiver')
