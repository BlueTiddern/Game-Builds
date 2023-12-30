"""
Definition of urls for DjangoFA.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views



urlpatterns = [
    path('', views.home, name='home'),
    path('bodyshape/', views.bodyshape_view, name='bodyshape'),
    path('skintype/', views.skintype_view, name='skintype'),
    path('figurefit/', views.figurefit, name='figurefit'),
    path('figure_fit/', views.figuref, name='figure_fit'),
    path('trends/', views.trends_view, name='trends'),
    path('menfalltrends2023/', views.trends_men_view, name='menfalltrends2023'),
    path('wintertrendswomen2023/', views.trends_women_view, name='wintertrendswomen2023'),
    path('spring2023trends/', views.trends_spring_view, name='spring2023trends'),
    path('customer_review/', views.customer, name='customer_review'),
    path('advisor/', views.advisor, name='advisor'),
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout_view, name='signout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    
]
    
