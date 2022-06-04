from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

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
        template_name='app/forms/driver_form.html'
    )
    
    
def auto_form(request):
    if request.method == 'POST':
        auto_form = AutoForm(request.POST or None)
        if auto_form.is_valid():
            data = auto_form.cleaned_data
            autos = Auto(brand=data['brand'],
                        model=data['model'],
                        year=data["year"])
            autos.save()

            autos = Auto.objects.all()
            context_dict = {'autos': autos}
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
        template_name='app/forms/car_form.html'
    )


def licencia_form(request):
    if request.method == 'POST':
        license_form = LicenciaForm(request.POST or None)
        
        if license_form.is_valid():
            data = license_form.cleaned_data
            licencias = Licencia(number=data['number'], 
                                 year=data['year'],
                                 owner=data['owner'])
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
        template_name='app/forms/license_form.html'
    )


def search(request):
    if request.GET['car_search']:
        search_param = request.GET['car_search']
        query = Q(brand__contains=search_param)
        query.add(Q(model__contains=search_param), Q.OR)
        query.add(Q(year__contains=search_param), Q.OR)
        autos = Auto.objects.filter(query)
        context_dict = {'autos': autos}
        
    elif request.GET['driver_search']:
        search_param = request.GET['driver_search']
        query = Q(full_name__contains=search_param)
        query.add(Q(day_of_birth__contains=search_param), Q.OR)
        query.add(Q(email__contains=search_param), Q.OR)
        query.add(Q(has_license__contains=search_param), Q.OR)
        conductores = Conductor.objects.filter(query)
        context_dict = {'conductores': conductores}
    
    elif request.GET['license_search']:
        search_param = request.GET['license_search']
        query = Q(number__contains=search_param)
        query.add(Q(year__contains=search_param), Q.OR)
        query.add(Q(owner__contains=search_param), Q.OR)
        licencias = Licencia.objects.filter(query)
        context_dict = {'licencias': licencias}

    # elif request.GET['all_search']:
    #     search_param = request.GET['license_search']
    #     query = Q(number__contains=search_param)
    #     query.add(Q(year__contains=search_param), Q.OR)
    #     query.add(Q(owner__contains=search_param), Q.OR)
    #     licencias = Licencia.objects.filter(query)
        
    #     search_param = request.GET['driver_search']
    #     query = Q(full_name__contains=search_param)
    #     query.add(Q(day_of_birth__contains=search_param), Q.OR)
    #     query.add(Q(email__contains=search_param), Q.OR)
    #     query.add(Q(has_license__contains=search_param), Q.OR)
    #     conductores = Conductor.objects.filter(query)
        
    #     search_param = request.GET['car_search']
    #     query = Q(brand__contains=search_param)
    #     query.add(Q(model__contains=search_param), Q.OR)
    #     query.add(Q(year__contains=search_param), Q.OR)
    #     autos = Auto.objects.filter(query)
        
    #     context_dict = {
    #         'all': licencias or conductores or autos
    #         }
        
    else:
        no = HttpResponse()
        context_dict = {'no':no}
        
        no2 = HttpResponse()
        context_dict = {'no2':no2}
        
        return render(request=request,
                      context=context_dict,
                      template_name="app/home.html")   
        
    return render(
        request=request,
        context=context_dict,
        template_name="app/home.html",
    )
