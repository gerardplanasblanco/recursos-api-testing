from django.db import models


class Autor(models.Model):
    nom = models.CharField(max_length=80)
    cognoms = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    data_naixement = models.DateField(blank=True, null=True)
    carrec = models.CharField(max_length=120, blank=True)

    class Meta:
        ordering = ['cognoms', 'nom']

    def __str__(self):
        return f"{self.nom} {self.cognoms}".strip()


class Recurs(models.Model):
    class Categoria(models.TextChoices):
        ARTICLE = 'article', 'Article'
        VIDEO = 'video', 'Vídeo'
        PODCAST = 'podcast', 'Podcast'
        CURS = 'curs', 'Curs'
        GUIA = 'guia', 'Guia'

    titol = models.CharField(max_length=150)
    descripcio = models.TextField(blank=True)
    categoria = models.CharField(max_length=20, choices=Categoria.choices)
    data_publicacio = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='recursos')

    class Meta:
        ordering = ['titol']

    def __str__(self):
        return self.titol
