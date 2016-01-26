# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recherche', '0002_auto_20160112_2231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pret',
            old_name='preteur',
            new_name='emprunteur',
        ),
        migrations.RemoveField(
            model_name='materiel',
            name='quantite',
        ),
        migrations.RemoveField(
            model_name='personne',
            name='identifiant',
        ),
        migrations.RemoveField(
            model_name='personne',
            name='objets',
        ),
        migrations.AddField(
            model_name='asso',
            name='team',
            field=models.ManyToManyField(to='recherche.Personne'),
        ),
    ]
