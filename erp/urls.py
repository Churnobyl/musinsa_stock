from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('erp/', views.erp, name='erp'),
    path('erp/<int:id>', views.detailed_erp, name='detail-erp'),
]
