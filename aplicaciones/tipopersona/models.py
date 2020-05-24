from django.db import models

class Tipopersona(models.Model):
    id      = models.AutoField(primary_key=True)
    tip_per = models.CharField(max_length=250, unique=True)
    usuario = models.CharField(max_length=30)
    opc_car = models.CharField(max_length=4)
    fec_car = models.DateField()
    hor_car = models.DateField()
    elimina = models.CharField(max_length=2)