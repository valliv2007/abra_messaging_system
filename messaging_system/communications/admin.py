from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    "messages in admin panel"
    list_display = ('id', 'sender', 'receiver', 'subject', 'creation_date', 'unread')
    list_filter = ('creation_date', 'unread')
    search_fields = ('sender__username', 'receiver__username', 'subject')
    list_editable = ('unread',)
