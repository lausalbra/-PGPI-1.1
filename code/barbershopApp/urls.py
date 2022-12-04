from django.urls import path
from barbershopApp import views

urlpatterns = [
   path('', views.home, name='home'),
   path('contacto/', views.contact, name = 'contact'),

   path('carrito/', views.carrito, name='carrito'),

   path('carrito/pago', views.pago, name='pago'),
   path('pago/tienda', views.pago_tienda, name='pago_tienda'),
   path('cargo/', views.cargo, name='cargo'),
   path('gracias/', views.gracias, name='gracias'),

   path('servicios/cortes', views.list_cortes, name = 'cortes'),
   path('servicios/barba', views.list_barbas, name = 'barbas'),
   path('servicios/tinte', views.list_tintes, name = 'tintes'),
   path('servicios/peinado', views.list_peinados, name = 'peinados'),
   path('servicios/estetica', views.list_esteticas, name = 'esteticas'),

   path('servicios/cortes/<int:servicio_id>/', views.details_corte, name='detalles_corte'),
   path('servicios/barba/<int:servicio_id>/', views.details_barba, name='detalles_barba'),
   path('servicios/tinte/<int:servicio_id>/', views.details_tinte, name='detalles_tinte'),
   path('servicios/peinado/<int:servicio_id>/', views.details_peinado, name='detalles_peinado'),
   path('servicios/estetica/<int:servicio_id>/', views.details_estetica, name='detalles_estetica'),

   path('terminos/', views.terminos, name='terminos'),
   path('registro/cliente', views.registro_cliente, name='registro'),

   path('servicios/tinte/seguimiento', views.seguimiento_tinte, name = 'seguimiento_tinte'),
   path('servicios/barba/seguimiento', views.seguimiento_barba, name = 'seguimiento_barba'),
   path('servicios/cortes/seguimiento', views.seguimiento_corte, name = 'seguimiento_corte'),
   path('servicios/peinado/seguimiento', views.seguimiento_peinado, name = 'seguimiento_peinado'),
   path('servicios/estetica/seguimiento', views.seguimiento_estetica, name = 'seguimiento_estetica'),


############################################ BARBA ADMIN #############################################  
   path('servicios/barbaAdmin', views.list_barbasAdmin, name = 'barbasAdmin'),
   path('servicios/barbaAdmin/<int:servicio_id>/', views.details_barbaAdmin, name='detalles_barbaAdmin'),
   path('servicios/crearBarbaAdmin', views.create_barba, name='create_barbaAdmin'), 
   path('deleteservicios/barbaAdmin/<int:servicio_id>/', views.borrarBarbas, name='delete_barba'),
   path('editServicios/barbaAdmin/<int:servicio_id>/', views.barba_update, name='update_barba'),
   path('indexAdmin', views.homeAdmin, name='indexAdmin'),
   
]