# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 16:46:20 2016

@author: Cindy
"""

from django.conf.urls import patterns, url
from account import views

 
urlpatterns = patterns('',
    url(r'^$', views.register, name='register'),
    url(r'^register/$',views.register,name = 'register'),
)