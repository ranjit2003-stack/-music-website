# Generated by Django 5.1.1 on 2025-03-14 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0013_music_dislikes_music_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=100)),
                ('price', models.IntegerField(null=True)),
                ('duration_days', models.IntegerField(null=True)),
            ],
        ),
    ]
