# Generated by Django 4.0.4 on 2022-05-09 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='static/images/default.jpg', null=True, upload_to='images/'),
        ),
    ]
