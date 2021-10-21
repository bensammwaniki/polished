from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("contact/", views.contact),
    path("adminst/", views.admin),
    
]
