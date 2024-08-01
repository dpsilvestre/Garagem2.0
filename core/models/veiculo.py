from django.db import models

from . import Cor, Modelo, Acessorio

class Veiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT)
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    acessorios = models.ManyToManyField(Acessorio)

    def __str__(self):
        return f"{self.modelo.nome}-{self.ano}-{self.cor.nome}"
    
    class Meta:
        """Meta options for the model."""

        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"