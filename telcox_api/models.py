from django.db import models

class Cliente(models.Model):
    mes = models.CharField(max_length=50)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    dato_usado = models.DecimalField(max_digits=10, decimal_places=2)
    minuto_usado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.mes
