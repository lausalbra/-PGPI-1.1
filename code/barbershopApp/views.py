from django.shortcuts import get_object_or_404, render

from .models import *
from PIL import Image

# Create your views here.

def home(request):
    return render(request, 'index.html')

def list_cortes(request):
    servicios = Cortes.objects.all()
    return render(request, 'cortes/cortes.html', {'cortes' : servicios})

def list_barbas(request):
    servicios = Barba.objects.all()
    return render(request, 'barbas/barba.html', {'barbas' : servicios})

def list_tintes(request):
    servicios = Tinte.objects.all()
    return render(request, 'tintes/tinte.html', {'tintes' : servicios})

def list_peinados(request):
    servicios = Peinado.objects.all()
    return render(request, 'peinados/peinado.html', {'peinados' : servicios})

def list_esteticas(request):
    servicios = Estética.objects.all()
    return render(request, 'esteticas/estetica.html', {'esteticas' : servicios})

############################################################################

def details_corte(request, servicio_id):
    servicio = get_object_or_404(Cortes, pk=servicio_id)
    image = Image.open(servicio.imagen)
    image.show()
    return render(request, 'cortes/detalles_corte.html', {'servicio': servicio})

def details_barba(request, servicio_id):
    servicio = get_object_or_404(Barba, pk=servicio_id)
    image = Image.open(servicio.imagen)
    image.show()
    return render(request, 'barbas/detalles_barba.html', {'servicio': servicio})

def details_tinte(request, servicio_id):
    servicio = get_object_or_404(Tinte, pk=servicio_id)
    image = Image.open(servicio.imagen)
    image.show()
    return render(request, 'tintes/detalles_tinte.html', {'servicio': servicio})

def details_peinado(request, servicio_id):
    servicio = get_object_or_404(Peinado, pk=servicio_id)
    image = Image.open(servicio.imagen)
    image.show()
    return render(request, 'peinados/detalles_peinado.html', {'servicio': servicio})

def details_estetica(request, servicio_id):
    servicio = get_object_or_404(Estética, pk=servicio_id)
    image = Image.open(servicio.imagen)
    image.show()
    return render(request, 'esteticas/detalles_estetica.html', {'servicio': servicio})