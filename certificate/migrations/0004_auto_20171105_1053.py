# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0003_auto_20171105_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenModelica_WS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=75)),
                ('purpose', models.CharField(default=b'OMW', max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Python_Workshop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('paper', models.CharField(max_length=300)),
                ('purpose', models.CharField(default=b'PWS', max_length=10)),
                ('college', models.CharField(max_length=200)),
                ('ws_date', models.CharField(max_length=100, null=True, blank=True)),
                ('is_coordinator', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Python_Workshop_BPPy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('paper', models.CharField(max_length=300)),
                ('purpose', models.CharField(default=b'PWS', max_length=10)),
                ('college', models.CharField(max_length=200)),
                ('ws_date', models.CharField(max_length=100, null=True, blank=True)),
                ('is_coordinator', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='event',
            name='purpose',
            field=models.CharField(max_length=25, choices=[(b'SLC', b'Scilab Conference'), (b'SPC', b'Scipy Conference'), (b'S16', b'Scipy 2016 Conference'), (b'PTC', b'Python Textbook Companion'), (b'STC', b'Scilab Textbook Companion'), (b'DCM', b'DrupalCamp Mumbai'), (b'FET', b'FreeEda Textbook Companion'), (b'OFC', b'OpenFOAM Symposium'), (b'FIC', b'Fossee Internship'), (b'F16', b'Fossee Internship 2016'), (b'OWS', b'Osdag Workshop'), (b'EWS', b'eSim Workshop'), (b'DRP', b'Drupal Workshop'), (b'OMW', b'OpenModelica Workshop'), (b'PWS', b'Python Workshop')]),
            preserve_default=True,
        ),
    ]
