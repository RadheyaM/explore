from django.urls import path
from . import views

urlpatterns = [
    path('', views.basket, name='basket')
]