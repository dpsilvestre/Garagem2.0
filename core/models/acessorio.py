from django.db import models

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
    class Meta:
        """Meta options for the model."""

        verbose_name = "Acessorio"
        verbose_name_plural = "Acessorios"