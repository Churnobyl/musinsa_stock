from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('erp/', views.erp, name='erp'),
    path('erp/<int:id>', views.detailed_erp, name='detail-erp'),
    path('erp/new', views.erp_goods_new, name='erp-goods-new'),
    path('erp/stock/<int:goods_id>', views.erp_goods_stock, name='erp-goods-stock'),
]
