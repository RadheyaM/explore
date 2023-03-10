# Generated by Django 3.2 on 2023-01-21 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20230121_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='body',
            field=models.TextField(help_text='Write your message here.', max_length=1064, verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(help_text='We will respond to this address.', max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='reason',
            field=models.CharField(help_text='Why are you contacting us today?', max_length=64, verbose_name='Message Subject'),
        ),
    ]
