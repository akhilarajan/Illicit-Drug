# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-04 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagramapp', '0007_police_drug_info_tb_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealer_info_tb',
            name='status',
            field=models.CharField(default='0', max_length=50),
        ),
    ]
