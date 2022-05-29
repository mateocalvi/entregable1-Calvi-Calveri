from django.urls import path

from app import views

urlpatterns = [
    path('', views.home),
    path('drivers', views.conductor, name='Drivers'),
]