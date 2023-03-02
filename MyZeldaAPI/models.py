from django.db import models


class Personnage(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom