from django.urls import path
from barbershopApp import views

urlpatterns = [
   path('', views.home, name='home'),
   path('<int:servicio_id>/', views.details, name='detalles')
]