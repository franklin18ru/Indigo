from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Indigo import settings
from .models import ProfileUser
from .models import Favourites
from property.models import Properties

# Create your views here.
@login_required
def index (request):
    if request.user.is_staff:
        return HttpResponseRedirect(request.GET.get('next', settings.STAFF_SVAEDI))

    query_set = Favourites.objects.filter(user_id=request.user.pk).values('property')
    favProperties = Properties.objects.filter(id__in=query_set)

    return render(request, 'userProfile/index.html', {
        'favourites': favProperties
    })

def profile(request):
    pass