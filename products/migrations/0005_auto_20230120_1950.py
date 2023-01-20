# Generated by Django 3.2 on 2023-01-20 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20230118_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(help_text='Book Author', max_length=64),
        ),
        migrations.AlterField(
            model_name='books',
            name='category',
            field=models.ForeignKey(default=1, help_text='Book Category', on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
        migrations.AlterField(
            model_name='books',
            name='code',
            field=models.CharField(blank=True, help_text='Unique 19 digit product code', max_length=19, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.TextField(help_text='Book Description'),
        ),
        migrations.AlterField(
            model_name='books',
            name='genre',
            field=models.ForeignKey(help_text='Book Genre', on_delete=django.db.models.deletion.CASCADE, to='products.genre'),
        ),
        migrations.AlterField(
            model_name='books',
            name='google_url',
            field=models.URLField(blank=True, help_text='A Url to the book on google books', max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Book Cover Image'),
        ),
        migrations.AlterField(
            model_name='books',
            name='image_url',
            field=models.URLField(blank=True, help_text='Image URL Address', max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Book Price', max_digits=6),
        ),
        migrations.AlterField(
            model_name='books',
            name='publisher',
            field=models.CharField(help_text='Book Publisher', max_length=64),
        ),
        migrations.AlterField(
            model_name='books',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, help_text='Book Rating', max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='subtitle',
            field=models.TextField(help_text='Book Subtitle', max_length=254),
        ),
        migrations.AlterField(
            model_name='books',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Book Cover Thumbnail Image'),
        ),
        migrations.AlterField(
            model_name='books',
            name='thumbnail_url',
            field=models.URLField(blank=True, help_text='Thumbnail Url Address', max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(help_text='The Book Title', max_length=254, verbose_name='Book Title'),
        ),
    ]