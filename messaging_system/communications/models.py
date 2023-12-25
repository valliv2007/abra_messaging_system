from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Message(models.Model):
    """message model"""
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender', verbose_name='Sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver', verbose_name='Receiver')
    message_text = models.TextField('Message', blank=False)
    subject = models.CharField('Subject', blank=False, max_length=150)
    creation_date = models.DateField('Creation date', auto_now_add=True)
    unread = models.BooleanField('Unread', blank=False, default=True)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ("-creation_date",)

    def __str__(self):
        return f' {self.sender.get_username()} send {self.subject} to {self.receiver.get_username()}'
