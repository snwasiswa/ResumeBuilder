# Generated by Django 4.1.4 on 2023-01-30 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]
