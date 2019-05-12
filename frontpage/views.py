from django.shortcuts import render

# Create your views here.

def index(request, user=None):
    return render(request, 'frontpage/index.html', {'user': request.user})