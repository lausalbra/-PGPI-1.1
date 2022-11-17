from django.shortcuts import get_object_or_404, render

from .models import Servicios

# Create your views here.

def home(request):
    servicios = Servicios.objects.all()
    return render(request, 'index.html', {'servicios' : servicios})

def details(request, servicio_id):
    servicio = get_object_or_404(Servicios, pk=servicio_id)
    return render(request, 'detalles.html', {'servicio': servicio})