# Generated by Django 5.0 on 2023-12-25 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communications', '0003_add_ordering_in_message_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='unread',
            field=models.BooleanField(default=True, verbose_name='Unread'),
        ),
    ]
