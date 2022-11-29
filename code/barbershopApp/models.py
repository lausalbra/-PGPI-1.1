from django.db import models

# Create your models here.

##########################SERVICIOS######################################################################

class Cortes(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    hora = models.DateTimeField(null=False)
    disponible = models.BooleanField(blank=False, null=False)
    imagen = models.ImageField(upload_to='barbershopApp/static/media', null=False, blank=False)
    descripcion = models.TextField(max_length=255, blank=False, null=False)
    precio = models.FloatField(null = False, blank=False)

class Barba(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    hora = models.DateTimeField(null=False)
    disponible = models.BooleanField(blank=False, null=False)
    imagen = models.ImageField(upload_to='barbershopApp/static/media', null=False, blank=False)
    descripcion = models.TextField(max_length=255, blank=False, null=False)
    precio = models.FloatField(null = False, blank=False)

class Tinte(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    hora = models.DateTimeField(null=False)
    disponible = models.BooleanField(blank=False, null=False)
    imagen = models.ImageField(upload_to='barbershopApp/static/media', null=False, blank=False)
    descripcion = models.TextField(max_length=255, blank=False, null=False)
    precio = models.FloatField(null = False, blank=False)

class Peinado(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    hora = models.DateTimeField(null=False)
    disponible = models.BooleanField(blank=False, null=False)
    imagen = models.ImageField(upload_to='barbershopApp/static/media', null=False, blank=False)
    descripcion = models.TextField(max_length=255, blank=False, null=False)
    precio = models.FloatField(null = False, blank=False)

class Estética(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    hora = models.DateTimeField(null=False)
    disponible = models.BooleanField(blank=False, null=False)
    imagen = models.ImageField(upload_to='barbershopApp/static/media', null=False, blank=False)
    descripcion = models.TextField(max_length=255, blank=False, null=False)
    precio = models.FloatField(null = False, blank=False)

##########################SEGUIMIENTO######################################################################

opciones_pago = [
    [0, "reservado"],
    [1, "pagado"],
    [2, "pendiente de pago"],
]

opciones_seguimiento = [
    [0, "servicio realizado"],
    [1, "servicio pendiente"],
]


class Seguimiento(models.Model):
    seguimiento_id = models.CharField(max_length=70)
    corte_id = models.ForeignKey(Cortes,on_delete=models.CASCADE)
    barba_id = models.ForeignKey(Barba,on_delete=models.CASCADE)
    tinte_id = models.ForeignKey(Tinte,on_delete=models.CASCADE)
    peinado_id = models.ForeignKey(Peinado,on_delete=models.CASCADE)
    estetica_id = models.ForeignKey(Estética,on_delete=models.CASCADE)
    pago = models.IntegerField(choices=opciones_pago)
    estado = models.IntegerField(choices=opciones_seguimiento)

##########################CLIENTE######################################################################

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellidos =  models.CharField(max_length=100, blank=False, null=False)
    fecha_nacimiento = models.DateField(blank=False, null=False)
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
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre