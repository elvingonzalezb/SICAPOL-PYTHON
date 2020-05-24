from django.db import models

class Tipoarma(models.Model):
    id            = models.AutoField(primary_key=True)
    nom_tipo_arma = models.CharField(max_length=50)
    ind_activo    = models.BooleanField(default=True)

