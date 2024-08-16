from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
