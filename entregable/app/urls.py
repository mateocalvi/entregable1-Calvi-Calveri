from django.urls import path

from app import views

urlpatterns = [
    path('', views.home),
    path('driver', views.conductores, name='Drivers'),
    path('car', views.autos, name='Cars'),
]