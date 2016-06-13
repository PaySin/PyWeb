# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    realname = models.CharField(max_length=50)    
    password = models.CharField(max_length=50)
    area = models.CharField(max_length=50)