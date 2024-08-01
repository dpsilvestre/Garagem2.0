from django.db import models

from . import Marca, Categoria

class Modelo(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome}-{self.marca.nome}"
    
    class Meta:
        """Meta options for the model."""

        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"