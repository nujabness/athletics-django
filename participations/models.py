from django.db import models

class Participation(models.Model):
    athlete = models.ForeignKey('athletes.athlete', on_delete=models.CASCADE, default="0")
    epreuve = models.ForeignKey('epreuves.epreuve', on_delete=models.CASCADE, default="0")
    medaille = models.ForeignKey('medailles.medaille', on_delete=models.CASCADE, default="0")
    resultat = models.CharField(max_length=100)

    def __str__(self):
        return self.resultat

