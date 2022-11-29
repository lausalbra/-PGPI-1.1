from django.urls import path
from barbershopApp import views

urlpatterns = [
   path('', views.home, name='home'),
   path('contacto/', views.contact, name = 'contact'),

   path('carrito/', views.carrito, name='carrito'),

   path('carrito/pago', views.pago, name='pago'),
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
   path('registro/cliente', views.registro_cliente, name='registro')
   
]