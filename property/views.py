from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Max
from property.models import Properties
from property.models import PropertyImage
from django import forms
from realtor.forms.propertyForm import PropertyCreateForm

# Create your views here.


def index(request):
    search = request.GET.get('search', None)
    properties = Properties.objects.all().order_by('streetName')


    if search != None:
        sizeFrom = request.GET.get('sizeFrom')
        sizeTo = request.GET.get('sizeTo')
        types = request.GET.getlist('type') # [] if nothin selected
        priceTo = request.GET.get('priceTo')
        priceFrom = request.GET.get('priceFrom')
        streetName = request.GET.get('streetName')
        zips = request.GET.getlist('zip')



        if sizeFrom != 'none':
            properties = properties.filter(squareMeter__gte=sizeFrom)
        if sizeTo != 'none':
            properties = properties.filter(squareMeter__lte=sizeTo)
        if priceFrom != 'none':
            properties = properties.filter(price__gte=priceFrom)
        if priceTo != 'none':
            properties = properties.filter(price__lte=priceTo)
        if streetName != '':
            properties = properties.filter(streetName__icontains=streetName)

        if len(types) != 0:
            properties = properties.filter(type__in=types)

        if len(zips) != 0:
            properties = properties.filter(zip__in=zips)
        # add search filtering here
    context = {'properties': properties}
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


# CHECK IN list
# my_model.objects.filter(creator__in=creator_list)

# my_filter_qs = Q()
# for creator in creator_list:
#     my_filter_qs = my_filter_qs | Q(creator=creator)
# my_model.objects.filter(my_filter_qs)


# GET LIST OF CHECKED CHECKBOXES
# request.POST.getlist('recommendations')