from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='aboutUs-index'),
    path('staffRealtor', views.staffRealtor, name='staffRealtor-index'),
    path('openHouse', views.openHouse, name='openHouse-index')
]