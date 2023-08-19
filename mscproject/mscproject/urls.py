from django.contrib import admin
from django.urls import path, include   # Import the include function
from django.conf.urls.static import settings, static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('basicapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)