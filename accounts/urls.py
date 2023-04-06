from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('sign-up/', views.signup, name='sign-up'),
    path('sign-in/', views.signin, name='sign-in'),
    path('logout/', views.logout, name='logout'),
]
