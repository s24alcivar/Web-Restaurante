from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class Project(models.Model):
    nombres = models.CharField(max_length=100, primary_key=True, verbose_name="Nombres", default='Nombre predeterminado')
    correo_electronico = models.EmailField(verbose_name="Correo Electrónico", default='correo_electronico_predeterminado@example.com')
    asunto = models.CharField(max_length=255, default='Asunto')
    mensaje = models.TextField(verbose_name="Escribe tu Mensaje", default='Mensaje predeterminado')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombres, self.mensaje)
        
    
