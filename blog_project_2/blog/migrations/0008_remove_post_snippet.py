# Generated by Django 4.0.4 on 2022-05-09 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_snippet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='snippet',
        ),
    ]
