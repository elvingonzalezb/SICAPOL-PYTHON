from django.db import models

class Usuario(models.Model):
    id       = models.AutoField(primary_key=True)
    login    = models.CharField(max_length=20)
    tipo     = models.CharField(max_length=20)
    nombre   = models.CharField(max_length=40)
    password = models.CharField(max_length=50)
    usuario  = models.CharField(max_length=20)
    correo   = models.EmailField(blank=True)
    elimina  = models.BooleanField(default=True)
