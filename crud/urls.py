from django.urls import path
from . import views

urlpatterns = [
    path('manage/', views.manage, name='manage_products'),
    path('create-book/', views.CreateBookView.as_view(), name='create_book'),
    path('create-poster/', views.CreatePosterView.as_view(), name='create_poster'),
    path('create-category/', views.CreateCategoryView.as_view(), name='create_category'),
    path('create-genre/', views.CreateGenreView.as_view(), name='create_genre'),
    path('update-book/<int:pk>/', views.UpdateBookView.as_view(), name='update_book'),
    path('update-poster/<int:pk>', views.UpdatePosterView.as_view(), name='update_poster'),
    path('update-category/<int:pk>', views.UpdateCategoryView.as_view(), name='update_category'),
    path('update-genre/<int:pk>', views.UpdateGenreView.as_view(), name='update_genre'),
    path('delete-book/<int:pk>/', views.DeleteBookView.as_view(), name='delete_book'),
    path('delete-poster/<int:pk>', views.DeletePosterView.as_view(), name='delete_poster'),
    path('delete-category/<int:pk>', views.DeleteCategoryView.as_view(), name='delete_category'),
    path('delete-genre/<int:pk>', views.DeleteGenreView.as_view(), name='delete_genre'),
]