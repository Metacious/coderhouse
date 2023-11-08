from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    parentezco_conmigo = models.CharField(max_length=256)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    rut = models.IntegerField(max_length=16, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}, {self.nombre}, {self.parentezco_conmigo}"

