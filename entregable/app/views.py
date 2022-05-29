from urllib import request
from django.shortcuts import render

from app.models import Conductor

# Create your views here.


def home(request):
    return render(request,'app/home.html')


def conductor(request):
    conductor = Conductor.objects.all()

    context_dict = {'conductor': conductor}

    return render(
        request=request,
        context=context_dict,
        template_name="app/drivers.html",
    )




