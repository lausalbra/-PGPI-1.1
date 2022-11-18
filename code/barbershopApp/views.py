from django.shortcuts import get_object_or_404, redirect, render

from .forms import *

from .models import *
from PIL import Image
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

##########################################LISTs##########################################

def list_cortes(request):
    queryset=request.GET.get("buscar")
    servicios = Cortes.objects.filter(
            Q(disponible = True))
    if queryset:
        servicios = Cortes.objects.filter(
            Q(nombre__icontains = queryset)
        ).distinct()
    return render(request, 'cortes/cortes.html', {'cortes' : servicios})

def list_barbas(request):
    queryset=request.GET.get("buscar")
    servicios = Barba.objects.filter(
            Q(disponible = True))
    if queryset:
        servicios = Barba.objects.filter(
            Q(nombre__icontains = queryset)
        ).distinct()
    return render(request, 'barbas/barba.html', {'barbas' : servicios})

def list_tintes(request):
    queryset=request.GET.get("buscar")
    servicios = Tinte.objects.filter(
            Q(disponible = True))
    if queryset:
        servicios = Tinte.objects.filter(
            Q(nombre__icontains = queryset)
        ).distinct()
    return render(request, 'tintes/tinte.html', {'tintes' : servicios})

def list_peinados(request):
    queryset=request.GET.get("buscar")
    servicios = Peinado.objects.filter(
            Q(disponible = True))
    if queryset:
        servicios = Peinado.objects.filter(
            Q(nombre__icontains = queryset)
        ).distinct()
    return render(request, 'peinados/peinado.html', {'peinados' : servicios})

def list_esteticas(request):
    queryset=request.GET.get("buscar")
    servicios = Estética.objects.filter(
            Q(disponible = True))
    if queryset:
        servicios = Estética.objects.filter(
            Q(nombre__icontains = queryset)
        ).distinct()
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
    