from django.contrib import admin
from .models import Category, Genre, Books, Posters

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Books)
admin.site.register(Posters)
