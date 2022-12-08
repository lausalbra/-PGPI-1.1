from django.db import models

# Create your models here.

##########################SERVICIOS######################################################################

opciones_pago = [
    [0, "reservado"],
    [1, "pagado"],
    [2, "pendiente de pago"],
    [3, "disponible"],
]

opciones_seguimiento = [
    [0, "servicio realizado"],
    [1, "servicio pendiente"],
]

class Cortes(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    hora = models.DateTimeField(null=False, help_text="Año-Mes-Dia Hora:Minuto")
    disponible = models.BooleanField(blank=False, null=False)
    imagen = models.ImageField(upload_to='media', null=False, blank=False)
    descripcion = models.TextField(max_length=255, blank=False, null=False)
    precio = models.FloatField(null = False, blank=False)
    pago = models.IntegerField(choices=opciones_pago, null=True)
    estado = models.IntegerField(choices=opciones_seguimiento, null=True)

class Barba(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    hora = models.DateTimeField(null=False, help_text="Año-Mes-Dia Hora:Minuto")
    disponible = models.BooleanField(blank=False, null=False)
    imagen = models.ImageField(upload_to='media', null=False, blank=False)
    descripcion = models.TextField(max_length=255, blank=False, null=False)
    precio = models.FloatField(null = False, blank=False)
    pago = models.IntegerField(choices=opciones_pago, null=True)
    estado = models.IntegerField(choices=opciones_seguimiento, null=True)

class Tinte(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    hora = models.DateTimeField(null=False, help_text="Año-Mes-Dia Hora:Minuto")
    disponible = models.BooleanField(blank=False, null=False)
    imagen = models.ImageField(upload_to='media', null=False, blank=False)
    descripcion = models.TextField(max_length=255, blank=False, null=False)
    precio = models.FloatField(null = False, blank=False)
    pago = models.IntegerField(choices=opciones_pago, null=True)
    estado = models.IntegerField(choices=opciones_seguimiento, null=True)
    
class Peinado(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    hora = models.DateTimeField(null=False, help_text="Año-Mes-Dia Hora:Minuto")
    disponible = models.BooleanField(blank=False, null=False)
    imagen = models.ImageField(upload_to='media', null=False, blank=False)
    descripcion = models.TextField(max_length=255, blank=False, null=False)
    precio = models.FloatField(null = False, blank=False)
    pago = models.IntegerField(choices=opciones_pago, null=True)
    estado = models.IntegerField(choices=opciones_seguimiento, null=True)

class Estética(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    hora = models.DateTimeField(null=False, help_text="Año-Mes-Dia Hora:Minuto")
    disponible = models.BooleanField(blank=False, null=False)
    imagen = models.ImageField(upload_to='media', null=False, blank=False)
    descripcion = models.TextField(max_length=255, blank=False, null=False)
    precio = models.FloatField(null = False, blank=False)
    pago = models.IntegerField(choices=opciones_pago, null=True)
    estado = models.IntegerField(choices=opciones_seguimiento, null=True)

##########################CLIENTE######################################################################

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellidos =  models.CharField(max_length=100, blank=False, null=False)
    fecha_nacimiento = models.DateField(blank=False, null=False, help_text="Año-Mes-Dia")
    email = models.EmailField(blank=False, null=False, unique=True)

################################################FORMULARIO DE CONTACTO##############################3

opciones_conultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_conultas)
    mensaje = models.TextField()
    

    def __str__(self):
        return self.nombre