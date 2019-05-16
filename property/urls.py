from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('offer', views.offer, name='offer'),
    path('paymentInfo', views.paymentInfo, name='paymentInfo'),
    path('overview', views.overview, name='overview'),
]