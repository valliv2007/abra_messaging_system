# Generated by Django 5.0 on 2023-12-25 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communications', '0002_alter_subject_in_message_model'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('-creation_date',), 'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
    ]