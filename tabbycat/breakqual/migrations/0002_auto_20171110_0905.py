# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 09:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('participants', '0001_initial'),
        ('breakqual', '0001_initial'),
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='breakingteam',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participants.Team', verbose_name='team'),
        ),
        migrations.AddField(
            model_name='breakcategory',
            name='breaking_teams',
            field=models.ManyToManyField(through='breakqual.BreakingTeam', to='participants.Team', verbose_name='breaking teams'),
        ),
        migrations.AddField(
            model_name='breakcategory',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament', verbose_name='tournament'),
        ),
        migrations.AlterUniqueTogether(
            name='breakingteam',
            unique_together=set([('break_category', 'team')]),
        ),
        migrations.AlterUniqueTogether(
            name='breakcategory',
            unique_together=set([('tournament', 'seq'), ('tournament', 'slug')]),
        ),
        migrations.AlterIndexTogether(
            name='breakcategory',
            index_together=set([('tournament', 'seq')]),
        ),
    ]
