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
########################################################## Admin
class BarbaForm(ModelForm):
    class Meta:
        model = Barba
        fields = '__all__'

class CorteForm(ModelForm):
    class Meta:
        model = Cortes
        fields = '__all__'

class EsteticasForm(ModelForm):
    class Meta:
        model = Estética
        fields = '__all__'

class PeinadoForm(ModelForm):
    class Meta:
        model = Peinado
        fields = '__all__'

class TinteForm(ModelForm):
    class Meta:
        model = Tinte
        fields = '__all__'