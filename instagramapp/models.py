# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class register_tb(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    ipaddr=models.CharField(max_length=50,default='0')
class image_tb(models.Model):
    user_id=models.CharField(max_length=50)
    image_nm=models.CharField(max_length=200)
    status=models.CharField(max_length=50)
class text_tb(models.Model):
    user_id=models.CharField(max_length=50)
    text_post=models.CharField(max_length=550)
    status=models.CharField(max_length=50)
class dealer_info_tb(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    ipaddr=models.CharField(max_length=50,default='0')
    status=models.CharField(max_length=50,default='0')
class police_drug_info_tb(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    ipaddr=models.CharField(max_length=50,default='0')
    status=models.CharField(max_length=50,default='0')
