from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('', login_required(views.delivery_address), name='profile'),
    path('contact/', views.ContactUs.as_view(), name='contact'),
    path('site-review/', views.CreateSiteReview.as_view(), name='site_review'),
    path('order-history/', login_required(views.order_history), name='order_history'),
    path('order-history/<order_number>', login_required(views.order_history_detail), name='order_history_detail'),
    path('wishlist/', login_required(views.wishlist), name='wishlist'),
    path('wishlist/edit-book/<int:id>', views.edit_book_wishlist, name='edit_book_wishlist'),
    path('wishlist/edit-poster/<int:id>', views.edit_poster_wishlist, name='edit_poster_wishlist'),
    path('subscribe', views.subscribe, name='subscribe'),
] 