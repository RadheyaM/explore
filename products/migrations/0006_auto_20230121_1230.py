# Generated by Django 3.2 on 2023-01-21 12:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_auto_20230120_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='user_book_wishlist',
            field=models.ManyToManyField(blank=True, related_name='user_book_wishlist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='posters',
            name='user_poster_wishlist',
            field=models.ManyToManyField(blank=True, related_name='user_poster_wishlist', to=settings.AUTH_USER_MODEL),
        ),
    ]