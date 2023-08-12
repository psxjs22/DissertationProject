from django.contrib import admin
from django.urls import path, include   # Import the include function
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('basicapp.urls')),
]

