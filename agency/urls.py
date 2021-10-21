from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("contact/", views.contact),
    path("administ/", views.admin),
    path('bookings/', views.bookings, name='bookings.service'),
    
]
