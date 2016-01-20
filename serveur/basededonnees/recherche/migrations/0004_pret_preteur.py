# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recherche', '0003_auto_20160113_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='pret',
            name='preteur',
            field=models.ForeignKey(related_name='preteur', blank=True, to='recherche.Personne', null=True),
        ),
    ]
