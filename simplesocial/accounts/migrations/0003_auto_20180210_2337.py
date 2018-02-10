# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-10 18:07
from __future__ import unicode_literals

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_diagnosisinfo_u_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnosisinfo',
            name='BMI',
        ),
        migrations.RemoveField(
            model_name='diagnosisinfo',
            name='bp_high',
        ),
        migrations.RemoveField(
            model_name='diagnosisinfo',
            name='bp_low',
        ),
        migrations.RemoveField(
            model_name='diagnosisinfo',
            name='pulse_rate',
        ),
        migrations.RemoveField(
            model_name='diagnosisinfo',
            name='resp_rate',
        ),
        migrations.RemoveField(
            model_name='diagnosisinfo',
            name='temperature',
        ),
        migrations.AddField(
            model_name='diagnosisinfo',
            name='Diastolic_Blood_Pressure',
            field=models.DecimalField(decimal_places=2, default='', max_digits=5, validators=[accounts.models.validate_bp_low]),
        ),
        migrations.AddField(
            model_name='diagnosisinfo',
            name='Pulse_rate',
            field=models.DecimalField(decimal_places=2, default='', max_digits=5, validators=[accounts.models.validate_pr]),
        ),
        migrations.AddField(
            model_name='diagnosisinfo',
            name='Respiratory_rate',
            field=models.DecimalField(decimal_places=2, default='', max_digits=5, validators=[accounts.models.validate_rr]),
        ),
        migrations.AddField(
            model_name='diagnosisinfo',
            name='Sore_Throat',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=128),
        ),
        migrations.AddField(
            model_name='diagnosisinfo',
            name='Systolic_Blood_Pressure',
            field=models.DecimalField(decimal_places=2, default='', max_digits=5, validators=[accounts.models.validate_bp_high]),
        ),
        migrations.AddField(
            model_name='diagnosisinfo',
            name='Temperature',
            field=models.DecimalField(decimal_places=2, default='', max_digits=5, validators=[accounts.models.validate_temp]),
        ),
    ]
