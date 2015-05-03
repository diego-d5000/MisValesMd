# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0003_auto_20150417_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='person',
        ),
        migrations.AddField(
            model_name='person',
            name='group',
            field=models.ManyToManyField(to='contactos.Group'),
        ),
    ]
