from django.urls import path
from . import views

urlpatterns = [
    path('enviar/', views.procesar_contacto, name='procesar_contacto'),
]