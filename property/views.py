from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Max
from property.models import Properties
from property.models import PropertyImage
from property.models import PropertyZoneArea
from django import forms
from realtor.forms.propertyForm import PropertyCreateForm
from .forms import buyStepOneForm

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
    context = {'form':PropertyCreateForm()}
    if request.method == 'POST':
        print('postmethod')
        form = PropertyCreateForm(data=request.POST)
        print(request.POST['zip'])
        if form.is_valid():
            form.save()
            propertyId = Properties.objects.order_by('-id')[0]
            propertyImage = PropertyImage(image=(request.POST['image']), propertyId_id=propertyId.id)
            propertyImage.save()
            return redirect('property-index')
        #     else:
        #         errorMessages = {'Error': 'Þessi staður er ekki til!'}
        #         print('Þessi staður er ekki til')
        # else:
        #     errorMessages = {'Error': 'Þetta póstfang er ekki til!'}
        #     print('Þetta póstfang er ekki til!')
    # try:
    #     context['errorMessages'] = errorMessages
    #
    # except UnboundLocalError:
    #     pass

    return render(request, 'realtor/addProperty.html', context)


# CHECK IN list
# my_model.objects.filter(creator__in=creator_list)

# my_filter_qs = Q()
# for creator in creator_list:
#     my_filter_qs = my_filter_qs | Q(creator=creator)
# my_model.objects.filter(my_filter_qs)


# GET LIST OF CHECKED CHECKBOXES
# request.POST.getlist('recommendations')


def buyStepOne(request, id):
    if request.method == 'POST':
        form = buyStepOneForm(data=request.POST)
        if form.is_valid():
            buyer = form.save()
            return render(request, 'property/paymentInfo.html')
    else:
        form = buyStepOneForm()

    return render(request, 'property/buyContactInfo.html', {'form': form})


def paymentForm(request):
    if request.method == "POST":
        form = paymentForm(data=request.POST)
        if form.is_valid():

            return render(request, 'property/paymentInfo.html')
    else:
        form = paymentForm()

    return render(request, 'property/buyContactInfo.html', {'form': form})


def reviewForm(request):
    pass