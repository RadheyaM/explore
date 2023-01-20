from django.urls import path
from . import views

urlpatterns = [
    path('manage/', views.manage, name='manage_products'),
    path('create-book/', views.CreateBookView.as_view(), name='create_book'),
    path('create-poster/', views.CreatePosterView.as_view(), name='create_poster'),
    path('create-category/', views.CreateCategoryView.as_view(), name='create_category'),
    path('create-genre/', views.CreateGenreView.as_view(), name='create_genre'),
]