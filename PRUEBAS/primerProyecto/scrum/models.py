from datetime import timezone

from django.db import models
from django.utils import timezone

# Create your models here.
class Programador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    roles = {
        "Prog": "Programador",
        "Test": "Tester",
        "JP": "Jefe de producción"
    }
    rol = models.CharField(choices=roles, default="Prog")


    def __str__(self):
        return f"{self.id} {self.nombre} {self.apellido} {self.fecha_nacimiento} {self.rol}"


class Tarea(models.Model):
    nombreTarea = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=100)
    estimacion = models.IntegerField(null=True, blank=True)
    asignada = models.BooleanField(default=False)
    usuario = models.ForeignKey(Programador, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id} {self.nombreTarea} {self.descripcion} {self.estimacion} {self.asignada} {self.usuario}"

class Sprint(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateField(default=timezone.now())
    fecha_fin = models.DateField()
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id} {self.nombre} {self.fecha_inicio} {self.fecha_fin} {self.tarea}"