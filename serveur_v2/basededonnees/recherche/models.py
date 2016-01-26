from django.db import models
from datetime import datetime

# Create your models here.

class Personne(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    mdp = models.CharField(max_length=50)
    assos = models.ForeignKey('Asso', null=True, blank=True)

    def __str__(self):
        return self.prenom

class Asso(models.Model):
    nom = models.CharField(max_length=50)
    team = models.ManyToManyField(Personne)

    def __str__(self):
        return self.nom

class Materiel(models.Model):
    nom = models.CharField(max_length=50)
    etat = models.BooleanField()
    asso = models.ForeignKey('Asso')
    #pret = models.ManyToManyField(Personne, through='Pret')

    def __str__(self):
        return self.nom

class Pret(models.Model):
    date_pret = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Date de Pret")
    date_retour = models.DateTimeField(default=datetime.now(), auto_now=False, verbose_name="Date de Retour")
    materiel = models.ForeignKey('Materiel')
    preteur = models.ForeignKey('Personne', null=True, blank=True, related_name='preteur')
    emprunteur = models.ForeignKey('Personne')

    def __str__(self):
        return "{0} prete par {1} a {2}".format(self.materiel, self.preteur, self.emprunteur)

