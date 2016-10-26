# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 23:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=250)),
                ('apellido', models.CharField(blank=True, max_length=250)),
                ('edad', models.IntegerField(blank=True, default=0)),
                ('familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='familias.Familia')),
            ],
        ),
    ]
