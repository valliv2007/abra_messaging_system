from re import M
from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    "messages in admin panel"
    list_display = ('id', 'sender', 'receiver', 'subject', 'creation_date')
    list_filter = ('creation_date',)
    search_fields = ('sender__username', 'receiver__username', 'subject')
