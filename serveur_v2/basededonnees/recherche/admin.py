from django.contrib import admin

# Register your models here.

from .models import Materiel, Pret

admin.site.register(Materiel)
admin.site.register(Pret)
