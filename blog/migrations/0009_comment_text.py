# Generated by Django 3.0 on 2020-09-12 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default='1'),
            preserve_default=False,
        ),
    ]
