from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='property-index'),
    path('<int:id>', views.getPropertyById, name='property'),
    path('<int:id>/contactInfo', views.buyStepOne, name='StepOne'),
    path('<int:id>/paymentInfo', views.paymentForm, name='stepTwo'),
    path('review', views.reviewForm, name='finalStep')
]