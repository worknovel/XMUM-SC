# Generated by Django 3.0 on 2020-09-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='password',
            name='author',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
    ]
