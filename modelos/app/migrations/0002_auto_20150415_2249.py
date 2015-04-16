# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patos',
            name='color',
        ),
        migrations.AddField(
            model_name='especies',
            name='zona',
            field=models.CharField(default='ninguna', max_length=100),
            preserve_default=False,
        ),
    ]
