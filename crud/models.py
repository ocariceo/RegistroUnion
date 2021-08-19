from django.db import models

class Info(models.Model):
    
    
    nombre = models.CharField(max_length=200)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    escolaridad = models.CharField(max_length=200)
    comuna = models.CharField(max_length=200)
    contrato = models.CharField(max_length=2)
    vulnerabilidad = models.CharField(max_length=200)
    proyectable = models.CharField(max_length=2)    
    observaciones = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.nombre