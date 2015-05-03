# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0006_auto_20150420_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='direccion',
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Nombre'),
        ),
    ]
