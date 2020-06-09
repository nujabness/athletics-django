from django.db import models

class Nationalite(models.Model):
    nom_nationalite = models.CharField(max_length=100)
    link_nationalite = models.CharField(max_length=200)
    def __str__(self):
        return self.nom_nationalite

