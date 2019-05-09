from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'property/index.html')

def offer(request):
    return render(request, 'property/offer.html')