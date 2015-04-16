# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150416_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='pato',
            name='bd',
            field=models.DateTimeField(default='2015-01-02 01:15:25', auto_now_add=True),
            preserve_default=False,
        ),
    ]
