# Generated by Django 3.2 on 2023-01-28 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20230121_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='books',
            name='thumbnail_url',
        ),
    ]
