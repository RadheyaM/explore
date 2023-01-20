from django.urls import path
from . import views

urlpatterns = [
    path('create-book/', views.CreateBookView.as_view(), name='create_book')
]