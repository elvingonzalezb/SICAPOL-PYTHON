from django.db import models

class Actas(models.Model):
    corre_act = models.AutoField(primary_key = True)
    cod_ccp   = models.IntegerField()
    cod_est   = models.IntegerField()
    num_ofi   = models.CharField(max_length=50)
    cod_org   = models.IntegerField()
    x         = models.CharField(max_length=11)
    y         = models.CharField(max_length=11)
    fec_act   = models.CharField(max_length=11)
    hora      = models.IntegerField()
    minuto    = models.IntegerField()
    cod_reg   = models.IntegerField()
    cod_mcp   = models.IntegerField()
    cod_par   = models.IntegerField()
    cod_sec   = models.IntegerField()
    cal_ave   = models.CharField(max_length=11) 
    apt_cas   = models.CharField(max_length=11)
    pto_ref   = models.CharField(max_length=11)
    usuario   = models.CharField(max_length=11)
    opc_car   = models.CharField(max_length=11)
    fec_car   = models.IntegerField()
    hor_car   = models.DateField(auto_now=True)
    elimina   = models.CharField(max_length=11)

#envia un parametro por defecto
    def __str__(self):
        return self.usuario