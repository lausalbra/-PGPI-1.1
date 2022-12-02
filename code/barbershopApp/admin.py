from django.contrib import admin
from .models import Cortes, Barba, Tinte, Estética, Contacto, Cliente, Peinado

# Register your models here.

class ServiciosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'hora', 'disponible', 'descripcion', 'precio', 'pago', 'estado')
    list_filter = ('nombre', )
    search_fields = ('nombre', )
    icon_name = 'gamepad'

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'fecha_nacimiento', 'email')
    list_filter = ('nombre',)
    search_fields = ('nombre', )

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'tipo_consulta', 'mensaje', 'avisos')
    list_filter =  ('nombre',)
    search_fields = ('nombre', 'tipo_consulta')

admin.site.register(Cortes, ServiciosAdmin)
admin.site.register(Barba, ServiciosAdmin)
admin.site.register(Tinte, ServiciosAdmin)
admin.site.register(Peinado, ServiciosAdmin)
admin.site.register(Estética, ServiciosAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.site_header = 'Menú del admin de nuestra peluqueria'
admin.site.index_title = 'Panel de control de barbershop'
admin.site.site_title = 'Titulo en la pestaña del navegador'