from django.shortcuts import render, get_object_or_404
from property.models import Properties
from property.models import PropertyImage

# Create your views here.


def index(request):
    context = {'properties': Properties.objects.all().order_by('streetName')}
    return render(request, 'property/index.html', context)

def getPropertyById(request, id):
    return render(request, 'property/property.html', {
        'property': get_object_or_404(Properties, pk=id),
        'propertyimage2': get_object_or_404(PropertyImage, imagenum=2, propertyId_id=id),
        'propertyimage3': get_object_or_404(PropertyImage, imagenum=3, propertyId_id=id)
    })
