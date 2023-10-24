from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.db import models



class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30,blank=True, default='')
    logo = models.ImageField(upload_to='imagenes/')

    def __str__(self):
            texto="{0} ({1})"
            return texto.format(self.nombre,self.id)


    
class Comunicado(models.Model):
    TIPO_CHOICES = [
        ("S", "Suspension de actividades"),
        ("C", "Suspension de clase"),
        ("I", "Informacion"),
    ]
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    detalle = models.CharField(max_length=1000, blank=True, default='')
    detalle_corto = models.CharField(max_length=50, blank=True, default='')
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, default='I')
    fecha_publicacion = models.DateField(default=date.today)
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comunicados_creados',null=True,default=None)
    visible = models.BooleanField(default=True)
    fecha_modificacion = models.DateField(auto_now=True)

    def __str__(self):
        texto="{0} ({1}) {2}"
        return texto.format(self.titulo,self.id,self.publicado_por)



    
    