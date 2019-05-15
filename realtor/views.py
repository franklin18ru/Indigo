from django.shortcuts import render
from property.models import Properties

# Create your views here.


def index(request):
    context = {'properties': Properties.objects.all().order_by('streetName')}
    return render(request, 'realtor/realtor.html', context)


def getPropertyByRealtorId(request, id):
    context = {'property': get_object_or_404(Properties, pk=id)}
    return render(request, 'property/property.html', {'property': get_object_or_404(Properties, pk=id)})

def addProperty(request):
    return render(request, 'realtor/addProperty.html')