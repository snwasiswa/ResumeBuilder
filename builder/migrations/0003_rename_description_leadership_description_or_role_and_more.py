# Generated by Django 4.1.4 on 2023-01-27 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leadership',
            old_name='description',
            new_name='description_or_role',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='body',
            new_name='role',
        ),
    ]
