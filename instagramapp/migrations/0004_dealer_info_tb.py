# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-27 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagramapp', '0003_text_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='dealer_info_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
            ],
        ),
    ]
