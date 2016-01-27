from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from recherche.models import Materiel, Pret, Personne, Asso
from recherche.forms import MaterielForm
import json
import time

# Pour les questions de securite de POST
from django.views.decorators.csrf import csrf_exempt

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

def nouveau_mdp(request):
    preno = request.GET['prenom']
    no = request.GET['nom']
    mdp = request.GET['mdp']
    personne = Personne.objects.get(nom=no, prenom=preno)
    personne.mdp = mdp
    personne.save()
    ident = personne.id

    return HttpResponse(json.dumps({'resultat':'success', 'nom':personne.nom, 'prenom':personne.prenom, 'id':ident}), content_type='application/json')

def identification1(request):
    nom = request.GET['nom']
    mdp = request.GET['mdp']
    personne = Personne.objects.get(nom=nom)
    try:
        personne = Personne.objects.get(nom=nom)
    except (KeyError, Personne.DoesNotExist):
        return HttpResponse(json.dumps({'resultat':'no_id'}), content_type='application/json')

    if personne.mdp == mdp:
        return HttpResponse(json.dumps({'resultat':'success', 'nom':personne.nom, 'prenom':personne.prenom, 'id':personne.id}), content_type='application/json')

    else:
        return HttpResponse(json.dumps({'resultat':'mauvais mdp'}), content_type='application/json')

def identification(received_jason):
    nom = received_jason['pseudo']
    mdp = received_jason['motdepasse']
    personne = Personne.objects.get(nom=nom)
#    try:
#        personne = Personne.objects.get(nom=nom)
#    except (KeyError, Personne.DoesNotExist):
#        return HttpResponse(json.dumps({'resultat':'no_id'}), content_type='application/json')

    if personne.mdp == mdp:
        return HttpResponse(json.dumps({'resultat':'success', 'nom':personne.nom, 'prenom':personne.prenom, 'id':personne.id}), content_type='application/json')

    else:
        return HttpResponse(json.dumps({'resultat':'mauvais mdp'}), content_type='application/json')

def formulaire(received_jason):
    pseudoemprunteur = received_jason['pseudoemprunteur']
    assoemprunteur = received_jason['assoemprunteur']
    pseudopreteur = received_jason['pseudopreteur']
    assopreteur = received_jason['assopreteur']
    objet = received_jason['objet']
    dateretour = received_jason['dateretour']
    emprunteur = Personne.objects.get(nom=pseudoemprunteur)
    preteur = Personne.objects.get(nom=pseudopreteur)
    obj = Materiel.objects.get(nom=objet)

    if obj.asso != assopreteur:
        return HttpResponse(json.dumps({'resultat':'pas le droit de preter'}), content_type='application/json')

    if obj.etat:
        objet.etat=False
        pret = Pret(emprunteur=emprunteur, preteur=preteur, materiel= obj)
        pret.save()
        objet.save()
        return HttpResponse(json.dumps({'resultat':'success', 'nom':objet.nom, 'etat':objet.etat, 'asso':objet.asso.nom}), content_type='application/json')

    else:
        return HttpResponse(json.dumps({'resultat':'objet non dispo'}), content_type='application/json')

# Pour pouvoir activer la methode POST sans securite
@csrf_exempt
def index(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        received_json_data = json.loads(body_unicode)
        
        HttpResponse(json.dumps({ resultat: 'success'}), content_type='application/json')

        #if received_json_data['page'] == 'connexion':
        #    identification(received_json_data)
    
        #if received_json_data['page'] == 'formulaire':
        #    formulaire(received_json_data)










