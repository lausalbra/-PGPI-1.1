from django.forms import ModelForm
from .models import *

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidos', 'fecha_nacimiento', 'email']

####################################################FORMNULARIO DE CONTACTO

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'