# Generated by Django 5.1.1 on 2025-02-03 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_music_genre_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='image',
            field=models.ImageField(default='Sample.jpg', upload_to='profiles'),
        ),
    ]
