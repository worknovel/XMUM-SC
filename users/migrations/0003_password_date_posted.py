# Generated by Django 3.0 on 2020-09-13 11:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_password_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='password',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
