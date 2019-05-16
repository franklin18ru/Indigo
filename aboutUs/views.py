from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from realtor.models import Realtors
from .forms import ContactForm

def index(request):
    return render(request, 'aboutUs/aboutUs.html')


def staffRealtor(request):
    context = {'realtors': Realtors.objects.all().order_by('name')}
    return render(request, 'aboutUs/staffRealtors.html', context)


def openHouse(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']
            sent = 'Netfang: ' + email +'\n' + 'Nafn: ' + str(name) + '\n' + 'skilaboð: ' + str(message)

            send_mail('Ný fyrirspurn frá indigofasteignir.is',
                      sent,
                      email,
                      ['indigofasteignir@gmail.com'],
                      fail_silently=False)
            return render(request, 'aboutUs/openHouseConfirm.html')
    else:
        form = ContactForm()

    return render(request, 'aboutUs/openHouse.html', {'form': form})

