from django.shortcuts import render
from realtor.models import Realtors


def index(request):
    return render(request, 'aboutUs/aboutUs.html')


def staffRealtor(request):
    context = {'realtors': Realtors.objects.all().order_by('name')}
    return render(request, 'aboutUs/staffRealtors.html', context)


def openHouse(request):
    return render(request, 'aboutUs/openHouse.html')
