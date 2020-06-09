from django.db import models

class Athlete(models.Model):
    nom_athlete = models.CharField(max_length=42)
    prenom_athlete = models.CharField(max_length=42)
    sexe_athlete = models.ForeignKey('athletes.sexe', on_delete=models.CASCADE, default="0")
    nationalite_athlete = models.ForeignKey('nationalites.nationalite', on_delete=models.CASCADE, default="0")

    def __str__(self):
        return self.nom_athlete + ' ' + self.prenom_athlete

class Sexe(models.Model):
    nom_sexe = models.CharField(max_length=10)

    def __str__(self):
        return self.nom_sexe