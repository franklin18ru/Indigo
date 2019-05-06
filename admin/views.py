from django.shortcuts import render


# Create your views here.

def index(response):
    return render(response, 'admin/index.html')