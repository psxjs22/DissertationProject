from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('method/', views.method, name='method'),
    path('consent/', views.consent_create, name='consent_create'),
    path('consent/<int:pk>/', views.consent_edit, name='consent_edit'),
    ]

