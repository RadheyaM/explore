from django.urls import path
from . import views

urlpatterns = [
    path('', views.basket, name='basket'),
    path('add/<item_id>', views.add_to_basket, name='add_to_basket'),
    path('remove/<item_id>/<material_size>/', views.remove_from_basket, name='remove_from_basket'),
]