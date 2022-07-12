from django.db import models

# Create your models here.


class Personas(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    rut=models.IntegerField(null=True)
    edad=models.IntegerField(null=True)
    comuna=models.CharField(max_length=10)
    email=models.EmailField(null=True)
    nombre_v=models.CharField(max_length=10,verbose_name="Vacuna")
    nro_dosis=models.IntegerField(verbose_name="Numero dosis")
    tfno=models.IntegerField(verbose_name="Telefono")
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido
     



class Usuario(models.Model):
    nombre=models.CharField(max_length=30)
    Contraseña=models.CharField(max_length=30)
    Contraseña2=models.CharField(max_length=30,default="Some String")
    Tipo_u=models.CharField(max_length=30,null=True)
    
    def __str__(self):
        return self.nombre 
    
    USERNAME_FIELD = 'nombre'
    REQUIRED_FIELDS = []
    

