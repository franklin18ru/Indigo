from django.shortcuts import render
from property.models import PropertyZoneArea

import sys

# Create your views here.

def index(request, user=None):
    regions = {'reykjavik': PropertyZoneArea.objects.all().filter(region='Reykjavík')
        ,'kopavogur': PropertyZoneArea.objects.all().filter(region='Kópavogur')
        ,'gardabaer': PropertyZoneArea.objects.all().filter(region='Garðabær')
        ,'hafnarfjordur': PropertyZoneArea.objects.all().filter(region='Hafnarfjörður')
        , 'mosfellsbaer': PropertyZoneArea.objects.all().filter(region='Mosfellsbær')
        , 'seltjarnarnes': PropertyZoneArea.objects.all().filter(region='Seltjarnarnes')
        , 'sudurnes': PropertyZoneArea.objects.all().filter(region='Suðurnes')
        , 'nordurland': PropertyZoneArea.objects.all().filter(region='Norðurland')
        , 'vestfirdir': PropertyZoneArea.objects.all().filter(region='Vestfirðir')
        , 'vesturland': PropertyZoneArea.objects.all().filter(region='Vesturland')
        , 'austurland': PropertyZoneArea.objects.all().filter(region='Austurland')
        , 'sudurland': PropertyZoneArea.objects.all().filter(region='Suðurland')
               }
    return render(request, 'frontpage/index.html', regions, {'user': request.user})

