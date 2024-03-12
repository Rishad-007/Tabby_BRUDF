# Generated by Django 2.1.2 on 2018-11-26 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0008_remove_deprecated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulknotification',
            name='event',
            field=models.CharField(blank=True, choices=[('p', 'team points'), ('c', 'ballot confirmed'), ('f', 'feedback URL'), ('b', 'ballot URL'), ('u', 'landing page URL'), ('d', 'adjudicator draw released'), ('t', 'team registration'), ('a', 'adjudicator registration'), ('m', 'motion(s) released'), ('r', 'team draw released')], max_length=1, verbose_name='event'),
        ),
    ]
