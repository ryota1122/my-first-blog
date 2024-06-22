# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 16:46:30 2024

@author: RShir
"""

from django.urls import path
from . import views
urlpatterns =[
    path('',views.post_list, name ='post_list'),
    ]