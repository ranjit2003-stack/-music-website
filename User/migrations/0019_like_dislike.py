# Generated by Django 5.1.1 on 2025-03-03 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0018_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='dislike',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
