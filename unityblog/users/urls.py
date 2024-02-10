"""Urls for user loging"""
from django.urls import path
from .import views


urlpatterns = [
    path('signup/', views.signup, name='users-sign-up')
]
