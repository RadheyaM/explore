# Generated by Django 3.2 on 2023-01-21 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_wishlist_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
