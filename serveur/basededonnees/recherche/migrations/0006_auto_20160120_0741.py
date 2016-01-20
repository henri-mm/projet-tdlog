# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('recherche', '0005_pret_date_retour'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='assos',
            field=models.ForeignKey(blank=True, to='recherche.Asso', null=True),
        ),
        migrations.AlterField(
            model_name='pret',
            name='date_retour',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 20, 7, 41, 55, 489815), verbose_name=b'Date de Retour'),
        ),
    ]
