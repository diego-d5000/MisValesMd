# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=200)),
                ('habitat', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('sexo', models.IntegerField(choices=[(1, b'Masculino'), (2, b'Femenino')])),
                ('color', models.CharField(default=b'amarillo', max_length=100, blank=True)),
                ('curp', models.CharField(unique=True, max_length=20)),
                ('especie', models.ForeignKey(to='app.Especies')),
            ],
        ),
    ]
