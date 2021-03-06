from django.shortcuts import render, get_object_or_404,redirect, HttpResponseRedirect
from django.db.models import Max
from property.models import Properties
from property.models import PropertyImage
from property.models import PropertyZoneArea
from django import forms
from realtor.forms.propertyForm import PropertyCreateForm
from userProfile.models import Favourites
from Indigo import settings
from .forms import buyStepOneForm, PaymentForm
from django.contrib.auth.decorators import login_required

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

    if request.method == 'POST':
        if request.user.is_anonymous:
            return HttpResponseRedirect(request.GET.get('next', settings.LOGIN_REDIRECT_URL))
        propid = request.POST.get('fav')

        if Favourites.objects.filter(user_id=request.user.pk, property_id=propid).exists():
            unfav = Favourites.objects.get(user_id=request.user.pk, property_id=propid)
            unfav.delete()
        else:
            Favourites.objects.create(user_id=request.user.pk, property_id=propid)

    if request.user.is_anonymous:
        context = {'properties': properties}
    else:
        query_set = Favourites.objects.filter(user_id=request.user.pk)
        values = query_set.values('id', 'user', 'property')
        print(values)
        context = {'properties': properties, 'favourites': values}
    return render(request, 'property/index.html', context)

def getPropertyById(request, id):
    return render(request, 'property/property.html', {
        'property': get_object_or_404(Properties, pk=id),
    })

def createProperty(request):
    context = {'form':PropertyCreateForm()}
    if request.method == 'POST':
        form = PropertyCreateForm(data=request.POST)
        image = PropertyCreateForm(extra=request.POST.get('extra_field_count'))
        if form.is_valid():
            form.save()
            propertyId = Properties.objects.order_by('-id')[0]
            propertyImage = PropertyImage(image=(request.POST['image']), propertyId_id=propertyId.id)
            propertyImage.save()
            print(request.POST['extra_field_count'])
            for num in range(12):
                try:
                    (PropertyImage(image=request.POST['extra_field_'+str(num)], propertyId_id=propertyId.id)).save()
                except Exception:
                    continue

            return redirect('property-index')

    return render(request, 'realtor/addProperty.html', context)


@login_required
def buyStepOne(request, id):
    if request.method == 'POST':
        if 'info' in request.POST:
            cform = buyStepOneForm(data=request.POST)
            pForm = PaymentForm(data=request.POST)
            if cform.is_valid() and pForm.is_valid():
                buyer = cform
                personalInfo = pForm
                buyer.save()

                return render(request, 'property/buyContactInfo.html',
                              {'buyer': buyer, 'personalInfo': personalInfo, 'review': True})

        if 'buy' in request.POST:
            propTodel = Properties.objects.get(pk=id)
            propTodel.delete()
            return HttpResponseRedirect(request.GET.get('next', settings.LOGIN_REDIRECT_URL))
    else:
        ContactForm = buyStepOneForm()
        paymentForm = PaymentForm()


        return render(request, 'property/buyContactInfo.html', {'contactForm': ContactForm ,'paymentForm': paymentForm, 'info': True})



