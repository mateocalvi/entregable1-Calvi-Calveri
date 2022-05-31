from django.urls import path

from app import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('drivers', views.conductores, name='Drivers'),
    path('cars', views.autos, name='Cars'),
    path('licenses', views.licencias, name='Licenses'),
    path('driver_form', views.conductor_form, name='DriverForm'),
    path('license_form', views.licencia_form, name='LicenseForm'),
    path('car_form', views.auto_form, name='CarForm'),
    path('search', views.search, name='Search'),
]