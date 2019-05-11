from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='property-index'),
    path('<int:id>', views.getPropertyById, name='property')
]