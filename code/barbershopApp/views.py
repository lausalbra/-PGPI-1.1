from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail

from .carrito import Carrito
from .forms import *
from .models import *
from django.db.models import Q
from .context_processor import *

import stripe

stripe.api_key= 'sk_test_51M7HevKBgV3pJGUTG1vx5xjV9Ru0kiKRL18MESqFLPbJ2Ch8OROkZfKT2NExOv49hn008Frkf7gId1305x53YGAx00L46Hi2SK'

# Create your views here.

def home(request):
    return render(request, 'index.html')

def registro_cliente(request):
    if request.method == 'GET':
        return render(request, 'cliente.html', {'form' : ClienteForm})
    else:
        try:
            form = ClienteForm(request.POST)
            nuevo_cliente = form.save(commit= False)
            nuevo_cliente.save()
            return redirect('home')
        except ValueError:
            return render(request, 'cliente.html', {'form' : ClienteForm, 'error' : form.errors})

def contact(request):
    if request.method == 'GET':
        return render(request, 'contacto.html', {'form' : ContactoForm})
    else:
        try:
            form = ContactoForm(request.POST)
            nuevo_cliente = form.save(commit= False)
            nuevo_cliente.save()
            return redirect('home')
        except ValueError:
            return render(request, 'contacto.html', {'form' : ContactoForm, 'error' : form.errors})

##########################################LISTs##########################################

def list_cortes(request):
    queryset=request.GET.get("buscar")
    servicios = Cortes.objects.all()
    if queryset:
        servicios = Cortes.objects.filter(
            Q(nombre__icontains = queryset)
        ).distinct()
    return render(request, 'cortes/cortes.html', {'cortes' : servicios})

def list_barbas(request):
    queryset=request.GET.get("buscar")
    servicios = Barba.objects.all()
    if queryset:
        servicios = Barba.objects.filter(
            Q(nombre__icontains = queryset)
        ).distinct()
    return render(request, 'barbas/barba.html', {'barbas' : servicios})

def list_tintes(request):
    queryset=request.GET.get("buscar")
    servicios = Tinte.objects.all()
    if queryset:
        servicios = Tinte.objects.filter(
            Q(nombre__icontains = queryset)
        ).distinct()
    return render(request, 'tintes/tinte.html', {'tintes' : servicios})

def list_peinados(request):
    queryset=request.GET.get("buscar")
    servicios = Peinado.objects.all()
    if queryset:
        servicios = Peinado.objects.filter(
            Q(nombre__icontains = queryset)
        ).distinct()
    return render(request, 'peinados/peinado.html', {'peinados' : servicios})

def list_esteticas(request):
    queryset=request.GET.get("buscar")
    servicios = Estética.objects.all()
    if queryset:
        servicios = Estética.objects.filter(
            Q(nombre__icontains = queryset)
        ).distinct()
    return render(request, 'esteticas/estetica.html', {'esteticas' : servicios})

############################################################################SHOWs##################################

def details_corte(request, servicio_id):
    if request.method == 'GET':
        servicio = get_object_or_404(Cortes, pk=servicio_id)
        return render(request, 'cortes/detalles_corte.html', {'servicio': servicio})
    else:
        try:
            servicio = get_object_or_404(Cortes, pk=servicio_id)
            ##SETEAR ATRIBUTO ENN BBDD
            setattr(servicio, 'disponible', False)
            servicio.save()
            ###############################

            #############AGREGAR PRODUCTO AL CARRITO###############
            carrito = Carrito(request)
            carrito.agregar(servicio)
            ###############################

            return redirect('carrito')
        except ValueError:
            return render(request, 'cortes/detalles_corte.html', {'servicio': servicio})


def details_barba(request, servicio_id):
    if request.method == 'GET':
        servicio = get_object_or_404(Barba, pk=servicio_id)
        return render(request, 'barbas/detalles_barba.html', {'servicio': servicio})
    else:
        try:
            servicio = get_object_or_404(Barba, pk=servicio_id)
            ##SETEAR ATRIBUTO ENN BBDD
            setattr(servicio, 'disponible', False)
            servicio.save()
            ###############################

             #############AGREGAR PRODUCTO AL CARRITO###############
            carrito = Carrito(request)
            carrito.agregar(servicio)
            ###############################

            return redirect('carrito')
        except ValueError:
            return render(request, 'barbas/detalles_barba.html', {'servicio': servicio})


def details_tinte(request, servicio_id):
    if request.method == 'GET':
        servicio = get_object_or_404(Tinte, pk=servicio_id)
        return render(request, 'tintes/detalles_tinte.html', {'servicio': servicio})
    else:
        try:
            servicio = get_object_or_404(Tinte, pk=servicio_id)
            ##SETEAR ATRIBUTO ENN BBDD
            setattr(servicio, 'disponible', False)
            servicio.save()
            ###############################

             #############AGREGAR PRODUCTO AL CARRITO###############
            carrito = Carrito(request)
            carrito.agregar(servicio)
            ###############################

            return redirect('carrito')
        except ValueError:
            return render(request, 'tintes/detalles_tinte.html', {'servicio': servicio})


def details_peinado(request, servicio_id):
    if request.method == 'GET':
        servicio = get_object_or_404(Peinado, pk=servicio_id)
        return render(request, 'peinados/detalles_peinado.html', {'servicio': servicio})
    else:
        try:
            servicio = get_object_or_404(Peinado, pk=servicio_id)
            ##SETEAR ATRIBUTO ENN BBDD
            setattr(servicio, 'disponible', False)
            servicio.save()
            ###############################

            #############AGREGAR PRODUCTO AL CARRITO###############
            carrito = Carrito(request)
            carrito.agregar(servicio)
            ###############################

            return redirect('carrito')
        except ValueError:
            return render(request, 'peinados/detalles_peinado.html', {'servicio': servicio})


def details_estetica(request, servicio_id):
    if request.method == 'GET':
        servicio = get_object_or_404(Estética, pk=servicio_id)
        return render(request, 'peinados/detalles_peinado.html', {'servicio': servicio})
    else:
        try:
            servicio = get_object_or_404(Estética, pk=servicio_id)
            ##SETEAR ATRIBUTO ENN BBDD
            setattr(servicio, 'disponible', False)
            servicio.save()
            ###############################

             #############AGREGAR PRODUCTO AL CARRITO###############
            carrito = Carrito(request)
            carrito.agregar(servicio)
            ###############################

            return redirect('carrito')
        except ValueError:
            return render(request, 'esteticas/detalles_estetica.html', {'servicio': servicio})


######################################################CARRITO#############################################

def carrito(request):
    return render(request, 'carrito.html')

##########################################PASARELA DE PAGO####################################################

def pago(request):
    return render(request, 'pagos.html')

def cargo(request):
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        customer = stripe.Customer.create(
            email=email,
            name=nombre,
            source = request.POST['stripeToken']
        )

        precio = total_carrito(request)
        valor = precio.get('total_carrito')
        id_pedido = request.POST['stripeToken']

        charge = stripe.Charge.create(
            customer=customer,
            amount=valor*1000,
            currency='mxn',
            description = 'Pago realizado'
        )

        carrito = Carrito(request)
        carrito.limpiar_carrito()

        ###RECIBO DE EMAIL####

        subject = "Pago realizado"
        message = "Se ha realizado su pedido correctamente: \n La cantidad pagada es de: " + str(valor) + "€. \n Tu id del pedido es: " + str(id_pedido)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST['email']]

        send_mail(subject, message, email_from, recipient_list)

    return redirect('gracias')

def gracias(request):
    return render(request, 'gracias.html')


def pago_tienda(request):
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        email = request.POST["email"]

        precio = total_carrito(request)
        valor = precio.get('total_carrito')

        for key, value in request.session.items():
            if key == 'carrito':
                for id in value:
                    producto_id = value[id]["producto_id"]
                    message = "Se ha realizado su pedido correctamente: \n La cantidad a pagar es de: " + str(valor) + "€. \n El id de los pedidos son: " + str(producto_id)

        ###RECIBO DE EMAIL####

        subject = "Pendiente de pagar"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST['email']]

        send_mail(subject, message, email_from, recipient_list)

        carrito = Carrito(request)
        carrito.limpiar_carrito()

    return redirect('home')

############################################POLITICA################

def terminos(request):
    return render(request,'terminos.html')

############################################SEGUIMIENTOS################

def seguimiento_corte(request):
    queryset=request.GET.get("buscar")
    servicios = Cortes.objects.all()
    if queryset:
        servicios = Cortes.objects.filter(
            Q(id == queryset)
        )
    return render(request, 'cortes/seguimiento.html', {'seguimiento' : servicios})

def seguimiento_barba(request):
    queryset=request.GET.get("buscar")
    servicios = Barba.objects.all()
    if queryset:
        servicios = Barba.objects.filter(
            Q(id == queryset)
        )
    return render(request, 'barbas/seguimiento.html', {'seguimiento' : servicios})

def seguimiento_peinado(request):
    queryset=request.GET.get("buscar")
    servicios = Peinado.objects.all()
    if queryset:
        servicios = Peinado.objects.filter(
            Q(id__icontains = queryset)
        )
    return render(request, 'peinados/seguimiento.html', {'seguimiento' : servicios})

def seguimiento_tinte(request):
    queryset=request.GET.get("buscar")
    servicios = Tinte.objects.all()
    if queryset:
        servicios = Tinte.objects.filter(
            Q(id == queryset)
        )
    return render(request, 'tintes/seguimiento.html', {'seguimiento' : servicios})

def seguimiento_estetica(request):
    queryset=request.GET.get("buscar")
    servicios = Estética.objects.all()
    if queryset:
        servicios = Estética.objects.filter(
            Q(id == queryset)
        )
    return render(request, 'esteticas/seguimiento.html', {'seguimiento' : servicios})

