from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login-index'),
    path('<int:id>', views.getPropertyByRealtorId, name='property-details')
]