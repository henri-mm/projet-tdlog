# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('recherche', '0006_auto_20160120_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pret',
            name='date_pret',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de Pret'),
        ),
        migrations.AlterField(
            model_name='pret',
            name='date_retour',
            field=models.DateTimeField(verbose_name='Date de Retour', default=datetime.datetime(2016, 2, 3, 2, 9, 12, 85766)),
        ),
    ]
