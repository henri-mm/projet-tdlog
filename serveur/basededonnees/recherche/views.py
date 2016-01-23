from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from recherche.models import Materiel, Pret, Personne, Asso
from recherche.forms import MaterielForm
import json
import time

# Create your views here.

def accueil(request):
    """ Afficher tous le materiel """
    materiel = Materiel.objects.all()
    return render(request, 'recherche/accueil.html', {'tous_le_matos': materiel})

def selection(request, id):
    """ Afficher des informations sur l'objet """
    matos = get_object_or_404(Materiel, id=id)
    team = matos.asso.team.all()
    return render(request, 'recherche/selection.html', {'materiel':matos})

def materiel1(request):
    if request.method == "GET":
        form = MaterielForm(request.GET)

        if form.is_valid():
            materiel = Materiel()
            materiel.nom = form.cleaned_data['nom']
            materiel.etat = form.cleaned_data['etat']
            materiel.asso = form.cleaned_data['asso']
            materiel.save()
    else:
        form = MaterielForm()

    return render(request, 'recherche/materiel1.html', locals())

def retour_materiel(request):
    nom = request.GET['nom']
    objet = Materiel.objects.get(nom=nom)

    return HttpResponse(json.dumps({'resultat':'success', 'nom':objet.nom, 'etat':objet.etat, 'asso':objet.asso.nom}), content_type='application/json')

def nouveau_pret(request):
    matos = request.GET['matos']
    emprunteu = request.GET['emprunteur']
    preteu = request.GET['preteur']
#    datere = request.GET['dateretour']
    objet = Materiel.objects.get(nom=matos)
    emprunteur = Personne.objects.get(prenom=emprunteu)
    preteur = Personne.objects.get(prenom=preteu)
#    dateretour = time.strptime(datere, "%d_%b_%y")
    if objet.etat:
        objet.etat=False
        pret = Pret(emprunteur=emprunteur, preteur=preteur, materiel= objet)
        pret.save()
        objet.save()

    return HttpResponse(json.dumps({'resultat':'success', 'nom':objet.nom, 'etat':objet.etat, 'asso':objet.asso.nom}), content_type='application/json')
