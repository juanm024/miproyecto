from mailbox import NoSuchMailboxError
from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField (max_length=20)
    apellido = models.CharField (max_length=30)
    email = models.EmailField ()


class Profesor(models.Model):
    nombre = models.CharField (max_length=20)
    apellido = models.CharField (max_length=30)
    email = models.EmailField ()
    profesion = models.CharField (max_length=30)


class Curso(models.Model):
    nombre = models.CharField (max_length=20)
    camada = models.IntegerField ()


class Entregable(models.Model):
    nombre = models.CharField (max_length=20)
    fechaentrega = models.DateTimeField ()
    entregado = models.BooleanField ()