# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150415_2249'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Especies',
            new_name='Especie',
        ),
        migrations.RenameModel(
            old_name='Patos',
            new_name='Pato',
        ),
    ]
