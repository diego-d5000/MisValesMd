# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0005_auto_20150420_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='group',
            field=models.ManyToManyField(to='contactos.Group', null=True, blank=True),
        ),
    ]
