from django.db import models
from datetime import datetime

# Create your models here.

class Asso(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class Materiel(models.Model):
    nom = models.CharField(max_length=50)
    quantite = models.IntegerField()
    etat = models.BooleanField()
    asso = models.ForeignKey('Asso')

    def __str__(self):
        return self.nom

class Personne(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    identifiant = models.CharField(max_length=50)
    mdp = models.CharField(max_length=50)
    objets = models.ManyToManyField(Materiel, through='Pret')

    def __str__(self):
        return self.identifiant

class Pret(models.Model):
    date_pret = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Date de Pret")
    #date_retour = models.DateTimeField(default=datetime.date.today(), auto_now=False, verbose_name="Date de Retour")
    materiel = models.ForeignKey(Materiel)
    preteur = models.ForeignKey(Personne)
    #emprunteur = models.ForeignKey(Personne)
    #assos?

    def __str__(self):
        return "{0} prete par {1} a {2}".format(self.materiel, self.preteur, self.emprunteur)

