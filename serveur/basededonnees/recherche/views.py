from django.shortcuts import render, get_object_or_404
from django.http import Http404
from recherche.models import Materiel
from recherche.forms import MaterielForm

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

def nouveau_materiel(request):
    nom = request.GET['nom']

    return HttpResponse(json.dumps({'resultat':'success'}), content_type='application/json')
