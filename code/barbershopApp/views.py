from django.shortcuts import get_object_or_404, redirect, render

from .forms import *

from .models import *
from PIL import Image

# Create your views here.

def home(request):
    return render(request, 'index.html')

##########################################LISTs##########################################

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

############################################################################SHOWs##################################

def details_corte(request, servicio_id):
    if request.method == 'GET':
        servicio = get_object_or_404(Cortes, pk=servicio_id)
        image = Image.open(servicio.imagen)
        image.show()
        return render(request, 'cortes/detalles_corte.html', {'servicio': servicio, 'form' : ClienteForm})
    else:
        try:
            servicio = get_object_or_404(Cortes, pk=servicio_id)
            form = ClienteForm(request.POST)
            nuevo_cliente = form.save(commit= False)
            nuevo_cliente.save()
            return redirect('home')
        except ValueError:
            return render(request, 'cortes/detalles_corte.html', {'servicio': servicio, 'form' : ClienteForm, 'error' : form.errors})


def details_barba(request, servicio_id):
    if request.method == 'GET':
        servicio = get_object_or_404(Barba, pk=servicio_id)
        image = Image.open(servicio.imagen)
        image.show()
        return render(request, 'barbas/detalles_barba.html', {'servicio': servicio, 'form' : ClienteForm})
    else:
        try:
            servicio = get_object_or_404(Barba, pk=servicio_id)
            form = ClienteForm(request.POST)
            nuevo_cliente = form.save(commit= False)
            nuevo_cliente.save()
            return redirect('home')
        except ValueError:
            return render(request, 'barbas/detalles_barba.html', {'servicio': servicio, 'form' : ClienteForm, 'error' : form.errors})



def details_tinte(request, servicio_id):
    if request.method == 'GET':
        servicio = get_object_or_404(Tinte, pk=servicio_id)
        image = Image.open(servicio.imagen)
        image.show()
        return render(request, 'tintes/detalles_tinte.html', {'servicio': servicio, 'form' : ClienteForm})
    else:
        try:
            servicio = get_object_or_404(Tinte, pk=servicio_id)
            form = ClienteForm(request.POST)
            nuevo_cliente = form.save(commit= False)
            nuevo_cliente.save()
            return redirect('home')
        except ValueError:
            return render(request, 'tintes/detalles_tinte.html', {'servicio': servicio, 'form' : ClienteForm, 'error' : form.errors})



def details_peinado(request, servicio_id):
    if request.method == 'GET':
        servicio = get_object_or_404(Peinado, pk=servicio_id)
        image = Image.open(servicio.imagen)
        image.show()
        return render(request, 'peinados/detalles_peinado.html', {'servicio': servicio, 'form' : ClienteForm})
    else:
        try:
            servicio = get_object_or_404(Peinado, pk=servicio_id)
            form = ClienteForm(request.POST)
            nuevo_cliente = form.save(commit= False)
            nuevo_cliente.save()
            return redirect('home')
        except ValueError:
            return render(request, 'peinados/detalles_peinado.html', {'servicio': servicio, 'form' : ClienteForm, 'error' : form.errors})



def details_estetica(request, servicio_id):
    if request.method == 'GET':
        servicio = get_object_or_404(Estética, pk=servicio_id)
        image = Image.open(servicio.imagen)
        image.show()
        return render(request, 'peinados/detalles_peinado.html', {'servicio': servicio, 'form' : ClienteForm})
    else:
        try:
            servicio = get_object_or_404(Estética, pk=servicio_id)
            form = ClienteForm(request.POST)
            nuevo_cliente = form.save(commit= False)
            nuevo_cliente.save()
            return redirect('home')
        except ValueError:
            return render(request, 'esteticas/detalles_estetica.html', {'servicio': servicio, 'form' : ClienteForm, 'error' : form.errors})
    