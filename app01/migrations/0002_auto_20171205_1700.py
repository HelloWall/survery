# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-05 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='option_trouble',
        ),
        migrations.AddField(
            model_name='option',
            name='option_trouble',
            field=models.ManyToManyField(related_name='option_trouble', to='app01.Trouble'),
        ),
    ]
