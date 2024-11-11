from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    datanascimento = models.DateField()

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name="Autor")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, verbose_name="Categoria"
    )
    numeropaginas = models.IntegerField(verbose_name="Número de Páginas")
