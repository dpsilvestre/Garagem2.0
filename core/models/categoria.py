from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        """Meta options for the model."""

        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"