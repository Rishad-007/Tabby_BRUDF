# Generated by Django 2.1.8 on 2019-07-28 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0004_auto_20180307_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venueconstraint',
            name='subject_content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'participants'), ('model', 'team')), models.Q(('app_label', 'participants'), ('model', 'adjudicator')), models.Q(('app_label', 'participants'), ('model', 'institution')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='subject content type'),
        ),
    ]
