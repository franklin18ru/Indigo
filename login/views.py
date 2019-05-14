from django.shortcuts import render, HttpResponseRedirect
from .forms import  RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from Indigo import settings
from django.conf import settings



# from django.contrib.admin.views.decorators import staff_member_required
#
# @staff_member_required



# {'redirect_authenticated_user': True}

def index(request):

    # checking if the user is already logged in then redirects the user to the front page
    checkuser = request.user
    check = checkuser.__class__.__name__
    if check != 'AnonymousUser':
        return HttpResponseRedirect(request.GET.get('next', settings.LOGIN_REDIRECT_URL))

    # Add message holder that goes with the render method
    # preferably two other holders one for login and the
    # other for register


    if request.method == 'POST' and 'login' in request.POST:
        form = AuthenticationForm(data=request.POST)
        # check the variables and see if they are valid,
        # if not then add error messages to the login
        # message holder
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect(request.GET.get('next', settings.LOGIN_REDIRECT_URL))
            #
        else:
            loginMessages = {'Error': 'Invalid username and/or password'}

    if request.method == 'POST' and 'register' in request.POST:
        form = RegisterForm(data=request.POST)
        # check the variables and see if they are valid,
        # if not then add error messages to the login
        # message holder
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(request.GET.get('next', settings.LOGIN_REDIRECT_URL))
        else:
            registerMessages = {'Error': 'Ógild nýskráning'}
    context = {'loginForm': AuthenticationForm(), 'registerForm': RegisterForm(), 'redirect_authenticated_user': True}

    try:
        if loginMessages:
            context['loginMessages'] =  loginMessages
    except UnboundLocalError:
        pass
    try:
        if registerMessages:
            context['registerMessages'] =  registerMessages
    except UnboundLocalError:
        pass

    return render(request, 'login/index.html', context)


def logoutView(request):
    logout(request)
    return HttpResponseRedirect(request.GET.get('next', settings.LOGIN_REDIRECT_URL))



def adminLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_staff:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/realtor'))
            else:
                loginMessages = {'Error': 'Notenda hefur ekki aðgang að þessari síðu'}
        else:
            loginMessages = {'Error': 'Ekki rétt netfang og/eða lykilorð'}
    context = {'loginForm': AuthenticationForm()}
    try:
        context['loginMessages'] = loginMessages
    except Exception:
        pass

    return render(request, 'realtor/realtorLogin.html', context)


