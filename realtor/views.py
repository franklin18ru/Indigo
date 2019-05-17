from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from property.models import Properties
from django.contrib.auth.decorators import login_required
from .models import Realtors
from .forms.updateRealtor import UpdateRealtor
from .forms.staffCreation import *
#
# @staff_member_required
# Create your views here.

@login_required
def index(request):
    if request.user.is_staff:
        # get realtor info based on email
        realtor = Realtors.objects.get(email=request.user.email)
        if request.method == 'POST':
            update = UpdateRealtor(data=request.POST, instance=realtor)
            if update.is_valid():
                print('is working')
                update.save()

        properties = Properties.objects.all().filter(realtor=realtor)
        form = UpdateRealtor(instance=realtor)
        context = {'properties': properties, 'realtor': realtor, 'form': form}
        return render(request, 'realtor/realtor.html', context)
    else:
        return HttpResponseRedirect(request.GET.get('next', '/userProfile'))


def getPropertyByRealtorId(request, id):
    context = {'property': get_object_or_404(Properties, pk=id)}
    return render(request, 'property/property.html', {'property': get_object_or_404(Properties, pk=id)})

def addProperty(request):
    return render(request, 'realtor/addProperty.html')

@login_required
def createRealtor(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = RegisterForm(data=request.POST)

            # check the variables and see if they are valid,
            # if not then add error messages to the login
            # message holder
            form.save(commit=False)

            if form.is_valid():
                name = request.POST.get('first_name')
                email = request.POST.get('username')
                position = request.POST.get('position')
                Realtors.objects.create(name=name, email=email)
                real = Realtors.objects.filter(email=email)


                form.is_staff = True
                form.save()

                return HttpResponseRedirect(request.GET.get('next', '/realtor/createRealtor'))


        return render(request, 'realtor/createRealtor.html', {
            'form': RegisterForm()
        })
    else:
        return HttpResponseRedirect(request.GET.get('next', '/'))


