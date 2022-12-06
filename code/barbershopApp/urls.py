from django.urls import path
from barbershopApp import views
from django.conf import settings
import django.views
from django.conf.urls.static import static

urlpatterns = [
   path('media/<path>', django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),
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

   ############################################ CORTE ADMIN #############################################  
   path('servicios/cortesAdmin', views.list_cortesAdmin, name = 'cortesAdmin'),
   path('servicios/cortesAdmin/<int:servicio_id>/', views.details_corteAdmin, name='detalles_corteAdmin'),
   path('servicios/crearCorteAdmin', views.create_corte, name='create_corteAdmin'), 
   path('deleteservicios/cortesAdmin/<int:servicio_id>/', views.borrarcortes, name='delete_corte'),
   path('editServicios/cortesAdmin/<int:servicio_id>/', views.corte_update, name='update_corte'),
   
   ############################################ ESTETICAS ADMIN #############################################  
   path('servicios/esteticasAdmin', views.list_esteticasAdmin, name = 'esteticasAdmin'),
   path('servicios/esteticasAdmin/<int:servicio_id>/', views.details_esteticaAdmin, name='detalles_esteticaAdmin'),
   path('servicios/crearEsteticaAdmin', views.create_estetica, name='create_esteticaAdmin'), 
   path('deleteservicios/esteticasAdmin/<int:servicio_id>/', views.borrarestetica, name='delete_estetica'),
   path('editServicios/esteticasAdmin/<int:servicio_id>/', views.estetica_update, name='update_estetica'),

   ############################################ PEINADO ADMIN #############################################  
   path('servicios/peinadosAdmin', views.list_peinadosAdmin, name = 'peinadoAdmin'),
   path('servicios/peinadosAdmin/<int:servicio_id>/', views.details_peinadosAdmin, name='detalles_peinadoAdmin'),
   path('servicios/crearPeinadoAdmin', views.create_peinado, name='create_peinadoAdmin'), 
   path('deleteservicios/peinadoAdmin/<int:servicio_id>/', views.borrarpeinado, name='delete_peinado'),
   path('editServicios/peinadoAdmin/<int:servicio_id>/', views.peinado_update, name='update_peinado'),

   ############################################ TINTE ADMIN #############################################  
   path('servicios/tinteAdmin', views.list_tinteAdmin, name = 'tinteAdmin'),
   path('servicios/tinteAdmin/<int:servicio_id>/', views.details_tinteAdmin, name='detalles_tinteAdmin'),
   path('servicios/crearTinteAdmin', views.create_tinte, name='create_tinteAdmin'), 
   path('deleteservicios/tinteAdmin/<int:servicio_id>/', views.borrartinte, name='delete_tinte'),
   path('editServicios/tinteAdmin/<int:servicio_id>/', views.tinte_update, name='update_tinte'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# agregado de static para permitir la visulaización de las imagenes desde la BD en las plantillas