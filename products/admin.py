from django.contrib import admin
from .models import Category, Genre, Books

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Books)

