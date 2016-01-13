from django.shortcuts import render
from django.http import Http404
from recherche.models import Materiel

# Create your views here.

def accueil(request):
    """ Afficher tous le materiel """
    materiel = Materiel.objects.all()
    return render(request, 'recherche/accueil.html', {'tous_le_matos': materiel})

def selection(request, id):
    """ Afficher des informations sur l'objet """
    pass
