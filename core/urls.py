from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('basket/', include('basket.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('crud/', include('crud.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404='home.views.handle_404'
handler403='home.views.handle_403'
handler500='home.views.handle_500'