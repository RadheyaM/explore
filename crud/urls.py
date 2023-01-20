from django.urls import path
from . import views

urlpatterns = [
    path('manage/', views.manage, name='manage_products'),
    path('create-book/', views.CreateBookView.as_view(), name='create_book'),
]