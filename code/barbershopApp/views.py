from django.shortcuts import get_object_or_404, render

from .models import Servicioss

# Create your views here.

def home(request):
    return render(request, 'index.html')

def list_servicios(request):
    servicios = Servicioss.objects.all()
    return render(request, 'servicios.html', {'servicios' : servicios})

def details(request, servicio_id):
    servicio = get_object_or_404(Servicioss, pk=servicio_id)
    return render(request, 'detalles.html', {'servicio': servicio})