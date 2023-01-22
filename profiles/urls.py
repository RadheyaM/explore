from django.urls import path
from . import views

urlpatterns = [
    path('', views.delivery_address, name='profile'),
    path('contact/', views.ContactUs.as_view(), name='contact'),
    path('site-review/', views.CreateSiteReview.as_view(), name='site_review'),
    path('order-history/', views.order_history, name='order_history'),
    path('order-history/<order_number>', views.order_history_detail, name='order_history_detail'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/edit-book/<int:id>', views.edit_book_wishlist, name='edit_book_wishlist'),
    path('wishlist/edit-poster/<int:id>', views.edit_poster_wishlist, name='edit_poster_wishlist'),
] 