from django.shortcuts import render

from app.models import Conductor

# Create your views here.


def index(ctx):
    return render(ctx,'app/home.html')


def conductor(ctx):
    conductor = Conductor.objects.all()

    context_dict = {'conductor': conductor}

    return render(
        request=ctx,
        context=context_dict,
        template_name="app/drivers.html",
    )




