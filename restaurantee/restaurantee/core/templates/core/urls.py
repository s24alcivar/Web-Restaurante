from django.urls import path
from .import views

urlpatterns = [ 
    path('', views.home),
    path('contacto/', views.contacto),
    path('crearContacto/', views.crearContacto),
    path('edicionContacto/<nombres>', views.edicionContacto),
    path('editarContacto/', views.editarContacto),
    path('eliminarContacto/<nombres>', views.eliminarContacto)
]