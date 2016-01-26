from django.shortcuts import render
from datetime import datetime

# Create your views here.

def date_actuelle(request):
   return render(request, 'polls/date.html', {'date': datetime.now()})

def addition(request, nombre1, nombre2):
    total = int(nombre1)+ int(nombre2)
    return render(request, 'polls/addition.html', locals())

from django.http import HttpResponse

def index(request):
    return HttpResponse("""Hello, world. You're at the poll index.""")
