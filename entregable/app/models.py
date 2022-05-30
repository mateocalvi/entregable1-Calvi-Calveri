from django.db import models

# Create your models here.

# TODO: Modelos : - Auto
#                 - Conductor 
#                 - Licencia

class Auto(models.Model):
    brand = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    year = models.IntegerField()
    
    def __str__(self) -> str:
        return f'Brand: {self.brand} | Model: {self.model} | Year: {self.year}'


class Conductor(models.Model):
    full_name = models.CharField(max_length=40)
    day_of_birth = models.CharField(max_length=40)
    email = models.EmailField()
    has_license = models.BooleanField()
    
    def __str__(self) -> str:
        has_license = 'Yes' if self.has_license else 'No'
        return f'Name: {self.full_name} | Day of birth: {self.day_of_birth} | Email: {self.email} | License?: {has_license} '


class Licencia(models.Model):
    number = models.CharField(max_length=40)
    year = models.IntegerField()
    owner = models.CharField(max_length=40)
    
    def __str__(self) -> str:
        return f'License number: {self.number} | Year: {self.year}'
