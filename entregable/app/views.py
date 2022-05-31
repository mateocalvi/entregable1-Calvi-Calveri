from urllib import request
from django.shortcuts import render

from app.models import Conductor, Auto, Licencia
from app.forms import ConductorForm, LicenciaForm, AutoForm

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

def licencias(request):
    licencias = Licencia.objects.all()

    context_dict = {'licencias': licencias}

    return render(
        request=request,
        context=context_dict,
        template_name="app/licenses.html",
    )

def conductor_form(request):
    if request.method == 'POST':
        conductor_form = ConductorForm(request.POST or None)
        
        if conductor_form.is_valid():
            data = conductor_form.cleaned_data
            conductores = Conductor(full_name=data['full_name'],
                                  day_of_birth=data['day_of_birth'],
                                  email=data["email"],
                                  has_license=data["has_license"]
                                  )
            conductores.save()

            conductores = Conductor.objects.all()
            context_dict = {'conductores': conductores}
            
            return render(
                request=request,
                context=context_dict,
                template_name="app/drivers.html"
            )

    conductor_form = ConductorForm(request.POST or None)
    context_dict = {'conductor_form': conductor_form}
    return render(
        request=request,
        context=context_dict,
        template_name='app/driver_form.html'
    )


def licencia_form(request):
    if request.method == 'POST':
        license_form = LicenciaForm(request.POST or None)
        
        if license_form.is_valid():
            data = license_form.cleaned_data
            licencias = Licencia(number=data['number'], 
                                 year=data['year'])
            licencias.save()
            
            licencias = Licencia.objects.all()
            context_dict = {'licencias': licencias}
            
            return render(
                request=request,
                context=context_dict,
                template_name="app/licenses.html"
            )

    license_form = LicenciaForm(request.POST or None)
    context_dict = {
        'license_form': license_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app/license_form.html'
    )


def auto_form(request):
    if request.method == 'POST':
        auto_form = AutoForm(request.POST or None)
        if auto_form.is_valid():
            data = auto_form.cleaned_data
            auto = Auto(brand=data['brand'],
                        model=data['model'],
                        year=data["year"])
            auto.save()

            auto = Auto.objects.all()
            context_dict = {
                'auto': auto
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app/cars.html"
            )

    auto_form = AutoForm(request.POST or None)
    context_dict = {'auto_form': auto_form}
    return render(
        request=request,
        context=context_dict,
        template_name='app/car_form.html'
    )



