# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 09:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('availability', '0001_initial'),
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roundavailability',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Round', verbose_name='round'),
        ),
        migrations.AlterUniqueTogether(
            name='roundavailability',
            unique_together=set([('round', 'content_type', 'object_id')]),
        ),
    ]
