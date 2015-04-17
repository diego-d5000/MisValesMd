from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.template.context_processors import csrf
from contactos import models as person_models


def home(request):
    return render(
        request,
        'index.html',
        {}
    )

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = UserCreationForm()
    return render(
        request, 'register.html', {'form': form}
    )


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect(reverse('address-book'))
        else:
            print 'trono'
    else:
        form = AuthenticationForm()
        return render(
            request,
            'login.html',
            {'form': form}
        )


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))