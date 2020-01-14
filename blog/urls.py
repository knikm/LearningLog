# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 19:16:57 2020

@author: KA
"""


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
