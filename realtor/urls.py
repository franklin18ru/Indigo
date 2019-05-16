from django.urls import path
from . import views
from property.views import createProperty

urlpatterns = [
    path('', views.index, name='realtor-index'),
    path('<int:id>', views.getPropertyByRealtorId, name='property-details'),
    path('addproperty', createProperty, name= 'property-addProperty')
]