from django.shortcuts import render
from property.models import Properties

# Create your views here.

def index(request):
    context = {'properties': Properties.objects.all().order_by('streetName')}
    return render(request, 'property/index.html', context)

def property(request):
    return render(request, 'property/property.html')