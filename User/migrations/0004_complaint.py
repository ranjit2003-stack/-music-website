# Generated by Django 5.1.1 on 2025-02-04 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_register_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
            ],
        ),
    ]
