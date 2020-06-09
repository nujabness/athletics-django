from django.db import models

class Medaille(models.Model):
    nom_medaille = models.CharField(max_length=42)
    link_medaille = models.CharField(max_length=200)

    def __str__(self):
        return self.nom_medaille

