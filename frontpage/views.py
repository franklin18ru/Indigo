from django.shortcuts import render, HttpResponseRedirect
from property.models import Properties

# Create your views here.

def index(request, user=None):
    # if 'search' in request.GET:
    #     streetName = request.GET['streetName']
    #     priceFrom = request.GET['priceFrom']
    #     priceTo = request.GET['priceTo']
    #     sizeFrom = request.GET['sizeFrom']
    #     sizeTo = request.GET['sizeTo']
    #     area = request.GET['area']
    #     type = request.GET['type']
    #     # Check each box and then create query with the url and send the user there
    #     query = {
    #         'streetName': streetName,
    #         'priceFrom': priceFrom,
    #         'priceTo': priceTo,
    #         'sizeFrom': sizeFrom,
    #         'sizeTo': sizeTo,
    #     }
    #     # add query to url
    #     return HttpResponseRedirect(request.GET.get('next', '/properties'))


    return render(request, 'frontpage/index.html', {'user': request.user})
