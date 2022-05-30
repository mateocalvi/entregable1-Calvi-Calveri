from urllib import request
from django.shortcuts import render

from app.models import Conductor, Auto, Licencia

# Create your views here.


def home(request):
    return render(request,'app/home.html')


def conductores(request):
    conductores = Conductor.objects.all()

    context_dict = {'conductores': conductores}

    return render(
        request=request,
        context=context_dict,
        template_name="app/drivers.html",
    )
    
def autos(request):
    autos = Auto.objects.all()

    context_dict = {'autos': autos}

    return render(
        request=request,
        context=context_dict,
        template_name="app/cars.html",
    )




