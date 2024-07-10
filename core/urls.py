from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.swagger import docs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.api_urls')),
    path('api-login/', include('rest_framework.urls')),
    path('docs/', docs.with_ui('swagger', cache_timeout=0), name="docs"),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
