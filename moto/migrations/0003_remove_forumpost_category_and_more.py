# Generated by Django 5.0.7 on 2024-07-25 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moto', '0002_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumpost',
            name='category',
        ),
        migrations.RemoveField(
            model_name='meetupevent',
            name='category',
        ),
    ]