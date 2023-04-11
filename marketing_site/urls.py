from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('privacy/', privacy, name='privacy'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('projects/', projects, name='projects'),
]
