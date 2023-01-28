from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = "Genre"

    def __str__(self):
        return self.name


class Books(models.Model):
    class Meta:
        verbose_name_plural = "Books"

    title = models.CharField(
        max_length=254, 
        verbose_name="Book Title", 
        help_text="The Book Title"
    )
    code = models.CharField(
        max_length=19, 
        null=True, 
        blank=True, 
        help_text="Unique 19 digit product code"
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        default=1, 
        help_text="Book Category"
    )
    author = models.CharField(
        max_length=64, help_text="Book Author")
    publisher = models.CharField(
        max_length=64, help_text="Book Publisher")
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, help_text="Book Genre")
    subtitle = models.TextField(
        max_length=254, help_text="Book Subtitle")
    description = models.TextField(help_text="Book Description")
    price = models.DecimalField(
        max_digits=6, decimal_places=2, help_text="Book Price")
    rating = models.DecimalField(
        max_digits=2, 
        decimal_places=1, null=True, blank=True, help_text="Book Rating"
    )
    google_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True,
        help_text="A Url to the book on google books",
    )
    thumbnail = models.ImageField(
        null=True, blank=True, verbose_name="Book Cover Thumbnail Image"
    )
    image = models.ImageField(
        null=True, blank=True, verbose_name="Book Cover Image")
    user_book_wishlist = models.ManyToManyField(
        User, related_name="user_book_wishlist", blank=True
    )

    def __str__(self):
        return self.title


class Posters(models.Model):
    class Meta:
        verbose_name_plural = "Posters"

    name = models.CharField(max_length=254)
    code = models.CharField(max_length=19, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    user_poster_wishlist = models.ManyToManyField(
        User, related_name="user_poster_wishlist", blank=True
    )

    def __str__(self):
        return self.name
