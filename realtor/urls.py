from django.urls import path
from . import views
from property.views import createProperty

urlpatterns = [
    path('', views.index, name='realtor-index'),
    path('<int:id>', views.getPropertyByRealtorId, name='property-details'),
    path('addProperty', createProperty, name='property-addProperty'),
    path('createRealtor', views.createRealtor, name='realtor-createRealtor')

]