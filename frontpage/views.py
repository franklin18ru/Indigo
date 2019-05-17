from django.shortcuts import render
import sys
from django.shortcuts import render, HttpResponseRedirect
from property.models import Properties
from property.models import PropertyZoneArea


# Create your views here.

def index(request, user=None):
    regions = {'reykjavik': PropertyZoneArea.objects.all().filter(region='Reykjavík').order_by('zip')
        ,'kopavogur': PropertyZoneArea.objects.all().filter(region='Kópavogur').order_by('zip')
        ,'gardabaer': PropertyZoneArea.objects.all().filter(region='Garðabær').order_by('zip')
        ,'hafnarfjordur': PropertyZoneArea.objects.all().filter(region='Hafnarfjörður').order_by('zip')
        , 'mosfellsbaer': PropertyZoneArea.objects.all().filter(region='Mosfellsbær').order_by('zip')
        , 'seltjarnarnes': PropertyZoneArea.objects.all().filter(region='Seltjarnarnes').order_by('zip')
        , 'sudurnes': PropertyZoneArea.objects.all().filter(region='Suðurnes').order_by('zip')
        , 'nordurland': PropertyZoneArea.objects.all().filter(region='Norðurland').order_by('zip')
        , 'vestfirdir': PropertyZoneArea.objects.all().filter(region='Vestfirðir').order_by('zip')
        , 'vesturland': PropertyZoneArea.objects.all().filter(region='Vesturland').order_by('zip')
        , 'austurland': PropertyZoneArea.objects.all().filter(region='Austurland').order_by('zip')
        , 'sudurland': PropertyZoneArea.objects.all().filter(region='Suðurland').order_by('zip')
               }
    return render(request, 'frontpage/index.html', regions, {'user': request.user})
