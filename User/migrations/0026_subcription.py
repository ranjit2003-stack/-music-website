# Generated by Django 5.1.1 on 2025-03-11 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0025_remove_register_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premium', models.IntegerField(max_length=50)),
            ],
        ),
    ]
