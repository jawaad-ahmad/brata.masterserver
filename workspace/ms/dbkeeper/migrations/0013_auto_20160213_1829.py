# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-13 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbkeeper', '0012_auto_20160116_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='registered',
            field=models.ForeignKey(default=b'', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teams', to='piservice.PiEvent'),
        ),
    ]
