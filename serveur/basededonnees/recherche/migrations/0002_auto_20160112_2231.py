# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recherche', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('identifiant', models.CharField(max_length=50)),
                ('mdp', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pret',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_pret', models.DateTimeField(auto_now=True, verbose_name=b'Date de Pret')),
                ('materiel', models.ForeignKey(to='recherche.Materiel')),
                ('preteur', models.ForeignKey(to='recherche.Personne')),
            ],
        ),
        migrations.AddField(
            model_name='personne',
            name='objets',
            field=models.ManyToManyField(to='recherche.Materiel', through='recherche.Pret'),
        ),
    ]
