from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('wishlist/view', views.wishlist, name='wishlist'),
    path('wishlist/edit-book/<int:id>', views.edit_book_wishlist, name='edit_book_wishlist'),
    path('wishlist/edit-poster/<int:id>', views.edit_poster_wishlist, name='edit_poster_wishlist'),
] 