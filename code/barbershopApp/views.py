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
            return redirect('formularioEnviado')
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
            return redirect('formularioEnviado')
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
        return render(request, 'cortes/detalles_corte.html', {'servicio': servicio, 'MEDIA_URL': settings.MEDIA_URL})
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
            return render(request, 'cortes/detalles_corte.html', {'servicio': servicio, 'MEDIA_URL': settings.MEDIA_URL})


def details_barba(request, servicio_id):
    if request.method == 'GET':
        servicio = get_object_or_404(Barba, pk=servicio_id)
        return render(request, 'barbas/detalles_barba.html', {'servicio': servicio, 'MEDIA_URL': settings.MEDIA_URL})
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
            return render(request, 'barbas/detalles_barba.html', {'servicio': servicio, 'MEDIA_URL': settings.MEDIA_URL})


def details_tinte(request, servicio_id):
    if request.method == 'GET':
        servicio = get_object_or_404(Tinte, pk=servicio_id)
        return render(request, 'tintes/detalles_tinte.html', {'servicio': servicio, 'MEDIA_URL': settings.MEDIA_URL})
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
            return render(request, 'tintes/detalles_tinte.html', {'servicio': servicio, 'MEDIA_URL': settings.MEDIA_URL})


def details_peinado(request, servicio_id):
    if request.method == 'GET':
        servicio = get_object_or_404(Peinado, pk=servicio_id)
        return render(request, 'peinados/detalles_peinado.html', {'servicio': servicio, 'MEDIA_URL': settings.MEDIA_URL})
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
            return render(request, 'peinados/detalles_peinado.html', {'servicio': servicio, 'MEDIA_URL': settings.MEDIA_URL})


def details_estetica(request, servicio_id):
    if request.method == 'GET':
        servicio = get_object_or_404(Estética, pk=servicio_id)
        return render(request, 'peinados/detalles_peinado.html', {'servicio': servicio, 'MEDIA_URL': settings.MEDIA_URL})
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
            return render(request, 'esteticas/detalles_estetica.html', {'servicio': servicio, 'MEDIA_URL': settings.MEDIA_URL})


######################################################CARRITO#############################################

def carrito(request):
    if request.method == 'GET':
        return render(request, 'carrito.html')
    else:
        carrito = Carrito(request)
        carrito.limpiar_carrito()
        return redirect('carrito')

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
        valor = int(precio.get('total_carrito'))
        id_pedido = request.POST['stripeToken']

        charge = stripe.Charge.create(
            customer=customer,
            amount=valor*1000,
            currency='mxn',
            description = 'Pago realizado'
        )

        for key, value in request.session.items():
            if key == 'carrito':
                for id in value:
                    producto_id = value[id]["producto_id"]
                    message = "Se ha realizado su pedido correctamente: \n La cantidad a pagar es de: " + str(valor) + "€. \n El id de los pedidos son: " + str(producto_id)

        ###RECIBO DE EMAIL####

        subject = "Pago realizado"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST['email']]

        send_mail(subject, message, email_from, recipient_list)

        carrito = Carrito(request)
        carrito.limpiar_carrito()

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

    return redirect('gracias')

############################################POLITICA################

def terminos(request):
    return render(request,'terminos.html')
############################################################
def formularioEnviado(request):
    return render(request,'formulario_enviado.html')


############################################SEGUIMIENTOS################

def seguimiento_corte(request):
    queryset=request.GET.get("buscar")
    servicios = []
    if queryset:
        servicios = Cortes.objects.filter(
            Q(id__icontains = queryset)
        )
    return render(request, 'cortes/seguimiento.html', {'seguimiento' : servicios})

def seguimiento_barba(request):
    queryset=request.GET.get("buscar")
    servicios = []
    if queryset:
        servicios = Barba.objects.filter(
            Q(id__icontains = queryset)
        )
    return render(request, 'barbas/seguimiento.html', {'seguimiento' : servicios})

def seguimiento_peinado(request):
    queryset=request.GET.get("buscar")
    servicios = []
    if queryset:
        servicios = Peinado.objects.filter(
            Q(id__icontains = queryset)
        )
    return render(request, 'peinados/seguimiento.html', {'seguimiento' : servicios})

def seguimiento_tinte(request):
    queryset=request.GET.get("buscar")
    servicios = []
    if queryset:
        servicios = Tinte.objects.filter(
            Q(id__icontains = queryset)
        )
    return render(request, 'tintes/seguimiento.html', {'seguimiento' : servicios})

def seguimiento_estetica(request):
    queryset=request.GET.get("buscar")
    servicios = []
    if queryset:
        servicios = Estética.objects.filter(
            Q(id__icontains = queryset)
        )
    return render(request, 'esteticas/seguimiento.html', {'seguimiento' : servicios})



############################# BARBA ADMIN ############################

def list_barbasAdmin(request):
    queryset=request.GET.get("buscar")
    servicios = Barba.objects.all()
    if queryset:
        servicios = Barba.objects.filter(
            Q(nombre__icontains = queryset)
        ).distinct()
    return render(request, 'barbas/barbaAdmin.html', {'barbas' : servicios, 'MEDIA_URL': settings.MEDIA_URL})

def details_barbaAdmin(request, servicio_id):
    if request.method == 'GET':
        servicio = get_object_or_404(Barba, pk=servicio_id)
        return render(request, 'barbas/barbaAdmin.html', {'servicio': servicio, 'MEDIA_URL': settings.MEDIA_URL})
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
            return render(request, 'barbas/barbaAdmin.html', {'servicio': servicio, 'MEDIA_URL': settings.MEDIA_URL})
            
def barba_update(request, servicio_id):
    if request.method == 'GET':
        barba = get_object_or_404(Barba, pk=servicio_id)
        form = BarbaForm(instance=barba)
        return render(request, 'barbas/update_barbaAdmin.html', {'barba': barba, 'form': form})
    else:
        try:
            barba = get_object_or_404(Barba, pk=servicio_id)
            form = BarbaForm(request.POST,request.FILES, instance=barba)
            form.save()
            return redirect('barbasAdmin')
        except ValueError:
            return render(request, 'barbas/update_barbaAdmin.html', {'barba': barba, 'form': BarbaForm,
                                                          'error': form.errors})
                                                  

def create_barba(request):
    if request.method == 'GET':
        return render(request, 'barbas/create_barbaAdmin.html', {'form': BarbaForm})
    else:
        try:
            form = BarbaForm(request.POST, request.FILES)
            nuevo_question = form.save(commit=False)
            nuevo_question.save()
            return redirect('barbasAdmin')
        except ValueError:
            return render(request, 'barbas/create_barbaAdmin.html', {'form': BarbaForm, 'error': form.errors})

def borrarBarbas(request, servicio_id):
    barba = Barba.objects.get(id = servicio_id)
    barba.delete()
    return redirect('barbasAdmin')


def homeAdmin(request):
    return render(request, 'indexAdmin.html')

############################# CORTE ADMIN ############################

def list_cortesAdmin(request):
    queryset=request.GET.get("buscar")
    servicios = Cortes.objects.all()
    if queryset:
        servicios = Cortes.objects.filter(
            Q(nombre__icontains = queryset)
        ).distinct()
    return render(request, 'cortes/cortesAdmin.html', {'cortes' : servicios, 'MEDIA_URL': settings.MEDIA_URL})

def details_corteAdmin(request, servicio_id):
    if request.method == 'GET':
        servicio = get_object_or_404(Cortes, pk=servicio_id)
        return render(request, 'cortes/cortesAdmin.html', {'servicio': servicio, 'MEDIA_URL': settings.MEDIA_URL})
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
            return render(request, 'cortes/cortesAdmin.html', {'servicio': servicio, 'MEDIA_URL': settings.MEDIA_URL})
            
def corte_update(request, servicio_id):
    if request.method == 'GET':
        cortes = get_object_or_404(Cortes, pk=servicio_id)
        form = CorteForm(instance=cortes)
        return render(request, 'cortes/update_corteAdmin.html', {'cortes': cortes, 'form': form})
    else:
        try:
            cortes = get_object_or_404(Cortes, pk=servicio_id)
            form = CorteForm(request.POST, request.FILES, instance=cortes)
            form.save()
            return redirect('cortesAdmin')
        except ValueError:
            return render(request, 'cortes/update_corteAdmin.html', {'cortes': cortes, 'form': CorteForm,
                                                          'error': form.errors})
                                                  

def create_corte(request):
    if request.method == 'GET':
        return render(request, 'cortes/create_corteAdmin.html', {'form': CorteForm})
    else:
        try:
            form = CorteForm(request.POST, request.FILES)
            nuevo_question = form.save(commit=False)
            nuevo_question.save()
            return redirect('cortesAdmin')
        except ValueError:
            return render(request, 'cortes/create_corteAdmin.html', {'form': CorteForm, 'error': form.errors})

def borrarcortes(request, servicio_id):
    cortes = Cortes.objects.get(id = servicio_id)
    cortes.delete()
    return redirect('cortesAdmin')


############################# esteticas ADMIN ############################

def list_esteticasAdmin(request):
    queryset=request.GET.get("buscar")
    servicios = Estética.objects.all()
    if queryset:
        servicios = Estética.objects.filter(
            Q(nombre__icontains = queryset)
        ).distinct()
    return render(request, 'esteticas/esteticasAdmin.html', {'esteticas' : servicios, 'MEDIA_URL': settings.MEDIA_URL})

def details_esteticaAdmin(request, servicio_id):
    if request.method == 'GET':
        servicio = get_object_or_404(Estética, pk=servicio_id)
        return render(request, 'esteticas/esteticasAdmin.html', {'servicio': servicio, 'MEDIA_URL': settings.MEDIA_URL})
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
            return render(request, 'esteticas/esteticasAdmin.html', {'servicio': servicio, 'MEDIA_URL': settings.MEDIA_URL})
            
def estetica_update(request, servicio_id):
    if request.method == 'GET':
        esteticas = get_object_or_404(Estética, pk=servicio_id)
        form = EsteticasForm(instance=esteticas)
        return render(request, 'esteticas/update_esteticaAdmin.html', {'esteticas': esteticas, 'form': form})
    else:
        try:
            esteticas = get_object_or_404(Estética, pk=servicio_id)
            form = EsteticasForm(request.POST,request.FILES, instance=esteticas)
            form.save()
            return redirect('esteticasAdmin')
        except ValueError:
            return render(request, 'esteticas/update_esteticaAdmin.html', {'esteticas': esteticas, 'form': EsteticasForm,
                                                          'error': form.errors})
                                                  

def create_estetica(request):
    if request.method == 'GET':
        return render(request, 'esteticas/create_esteticaAdmin.html', {'form': EsteticasForm})
    else:
        try:
            form = EsteticasForm(request.POST, request.FILES)
            nuevo_question = form.save(commit=False)
            nuevo_question.save()
            return redirect('esteticasAdmin')
        except ValueError:
            return render(request, 'esteticas/create_esteticaAdmin.html', {'form': EsteticasForm, 'error': form.errors})

def borrarestetica(request, servicio_id):
    barba = Estética.objects.get(id = servicio_id)
    barba.delete()
    return redirect('esteticasAdmin')

############################# peinado ADMIN ############################

def list_peinadosAdmin(request):
    queryset=request.GET.get("buscar")
    servicios = Peinado.objects.all()
    if queryset:
        servicios = Peinado.objects.filter(
            Q(nombre__icontains = queryset)
        ).distinct()
    return render(request, 'peinados/peinadoAdmin.html', {'peinados' : servicios, 'MEDIA_URL': settings.MEDIA_URL})

def details_peinadosAdmin(request, servicio_id):
    if request.method == 'GET':
        servicio = get_object_or_404(Peinado, pk=servicio_id)
        return render(request, 'peinados/peinadoAdmin.html', {'servicio': servicio, 'MEDIA_URL': settings.MEDIA_URL})
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
            return render(request, 'peinados/peinadoAdmin.html', {'servicio': servicio, 'MEDIA_URL': settings.MEDIA_URL})
            
def peinado_update(request, servicio_id):
    if request.method == 'GET':
        esteticas = get_object_or_404(Peinado, pk=servicio_id)
        form = PeinadoForm(instance=esteticas)
        return render(request, 'peinados/update_peinadoAdmin.html', {'peinado': esteticas, 'form': form})
    else:
        try:
            esteticas = get_object_or_404(Peinado, pk=servicio_id)
            form = PeinadoForm(request.POST, request.FILES, instance=esteticas)
            form.save()
            return redirect('peinadoAdmin')
        except ValueError:
            return render(request, 'peinados/update_peinadoAdmin.html', {'peinado': esteticas, 'form': PeinadoForm,
                                                          'error': form.errors})
                                                  

def create_peinado(request):
    if request.method == 'GET':
        return render(request, 'peinados/create_peinadoAdmin.html', {'form': PeinadoForm})
    else:
        try:
            form = PeinadoForm(request.POST, request.FILES)
            nuevo_question = form.save(commit=False)
            nuevo_question.save()
            return redirect('peinadoAdmin')
        except ValueError:
            return render(request, 'peinados/create_peinadoAdmin.html', {'form': PeinadoForm, 'error': form.errors})

def borrarpeinado(request, servicio_id):
    barba = Peinado.objects.get(id = servicio_id)
    barba.delete()
    return redirect('peinadoAdmin')

############################# tinte ADMIN ############################

def list_tinteAdmin(request):
    queryset=request.GET.get("buscar")
    servicios = Tinte.objects.all()
    if queryset:
        servicios = Tinte.objects.filter(
            Q(nombre__icontains = queryset)
        ).distinct()
    return render(request, 'tintes/tinteAdmin.html', {'tintes' : servicios, 'MEDIA_URL': settings.MEDIA_URL})

def details_tinteAdmin(request, servicio_id):
    if request.method == 'GET':
        servicio = get_object_or_404(Tinte, pk=servicio_id)
        return render(request, 'tintes/tinteAdmin.html', {'servicio': servicio, 'MEDIA_URL': settings.MEDIA_URL})
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
            return render(request, 'tintes/tinteAdmin.html', {'servicio': servicio, 'MEDIA_URL': settings.MEDIA_URL})
            
def tinte_update(request, servicio_id):
    if request.method == 'GET':
        esteticas = get_object_or_404(Tinte, pk=servicio_id)
        form = TinteForm(instance=esteticas)
        return render(request, 'tintes/update_tinteAdmin.html', {'tinte': esteticas, 'form': form})
    else:
        try:
            esteticas = get_object_or_404(Tinte, pk=servicio_id)
            form = TinteForm(request.POST,request.FILES,  instance=esteticas)
            form.save()
            return redirect('tinteAdmin')
        except ValueError:
            return render(request, 'tintes/update_tinteAdmin.html', {'tinte': esteticas, 'form': TinteForm,
                                                          'error': form.errors})
                                                  

def create_tinte(request):
    if request.method == 'GET':
        return render(request, 'tintes/create_tinteAdmin.html', {'form': TinteForm})
    else:
        try:
            form = TinteForm(request.POST, request.FILES)
            nuevo_question = form.save(commit=False)
            nuevo_question.save()
            return redirect('tinteAdmin')
        except ValueError:
            return render(request, 'tintes/create_tinteAdmin.html', {'form': TinteForm, 'error': form.errors})

def borrartinte(request, servicio_id):
    barba = Tinte.objects.get(id = servicio_id)
    barba.delete()
    return redirect('tinteAdmin')
