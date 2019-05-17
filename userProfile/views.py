from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Indigo import settings

# Create your views here.
@login_required
def index (request):
    if request.user.is_staff:
        return HttpResponseRedirect(request.GET.get('next', settings.STAFF_SVAEDI))

    return render(request, 'userProfile/index.html')