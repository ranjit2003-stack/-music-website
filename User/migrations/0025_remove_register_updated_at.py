# Generated by Django 5.1.1 on 2025-03-11 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0024_register_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='updated_at',
        ),
    ]
