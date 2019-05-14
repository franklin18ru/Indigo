from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Max
from property.models import Properties
from property.models import PropertyImage
from django import forms
from realtor.forms.propertyForm import PropertyCreateForm

# Create your views here.


def index(request):
    if 'search' in request:
        pass
    else:
        context = {'properties': Properties.objects.all().order_by('streetName')}
        return render(request, 'property/index.html', context)

def getPropertyById(request, id):
    return render(request, 'property/property.html', {
        'property': get_object_or_404(Properties, pk=id),
    })

def createProperty(request):
    if request.method == 'POST':
        form = PropertyCreateForm(data=request.POST)
        if form.is_valid():
            property = form.save()
            propertyId = Properties.objects.order_by('-id')[0]
            propertyImage = PropertyImage(image=(request.POST['image']), propertyId_id=propertyId.id)
            propertyImage.save()
            return redirect('property-index')
    else:
        form = PropertyCreateForm()
    return render(request, 'realtor/addProperty.html', {
        'form': form
    })