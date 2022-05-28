from django.urls import path

from app import views

urlpatterns = [
    path('', views.index),
    path('drivers', views.conductor, name='Drivers'),
]