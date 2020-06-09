from django.db import models

class Epreuve(models.Model):
    nom_epreuve = models.CharField(max_length=42)
    type_epreuve =  models.ForeignKey('epreuves.type', on_delete=models.CASCADE, default="0")
    phase_epreuve =  models.ForeignKey('epreuves.phase', on_delete=models.CASCADE, default="0")

    def __str__(self):
        return self.nom_epreuve

class Type(models.Model):
    nom_type = models.CharField(max_length=42)

    def __str__(self):
        return self.nom_type

class Phase(models.Model):
    nom_phase = models.CharField(max_length=42)

    def __str__(self):
        return self.nom_phase

