from django.db import models

# Create your models here.

class Servicioss(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    hora = models.DateTimeField(null=False)
    disponible = models.BooleanField(blank=False, null=False)
    imagen = models.ImageField(upload_to='barbershopApp/static/media', null=False, blank=False)
    descripcion = models.TextField(max_length=255, blank=False, null=False)
    precio = models.FloatField(null = False, blank=False)
