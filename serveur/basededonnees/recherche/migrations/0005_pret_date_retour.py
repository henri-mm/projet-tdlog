# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('recherche', '0004_pret_preteur'),
    ]

    operations = [
        migrations.AddField(
            model_name='pret',
            name='date_retour',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 19, 21, 39, 49, 85861), verbose_name=b'Date de Retour'),
        ),
    ]
