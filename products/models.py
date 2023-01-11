from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Genre'

    def __str__(self):
        return self.name


class Books(models.Model):

    class Meta:
        verbose_name_plural = 'Books'

    title = models.CharField(max_length=254)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.CharField(max_length=64)
    publisher = models.CharField(max_length=64)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    subtitle = models.TextField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    google_url = models.URLField(max_length=1024, null=True, blank=True)
    thumbnail_url = models.URLField(max_length=1024, null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title