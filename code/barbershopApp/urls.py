from django.urls import path
from barbershopApp import views

urlpatterns = [
   path('', views.home, name='home'),
   path('servicios', views.list_servicios, name = 'servicios'),
   path('servicios/cortes', views.list_servicios, name = 'cortes'),
   path('servicios/barba', views.list_servicios, name = 'barba'),
   path('servicios/tinte', views.list_servicios, name = 'tinte'),
   path('servicios/peinado', views.list_servicios, name = 'peinado'),
   path('servicios/estética', views.list_servicios, name = 'estética'),
   path('servicios/<int:servicio_id>/', views.details, name='detalles')
]