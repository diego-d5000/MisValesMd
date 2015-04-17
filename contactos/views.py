from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.template.context_processors import csrf
from .models import Person
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms as cForms


class PersonView(View):
    template_name = 'person.html'

    def get(self, request):
        form = cForms.PersonForm()
        return render(request, self.template_name, locals())

    def post(self, request):
        form = cForms.PersonForm(request.POST)

        if form.is_valid():
            form.save(user=request.user)
            return redirect('/')
        else:
            return render(request, self.template_name, locals())

    def dispatch(self, request, *args, **kwargs):
        return super(PersonView, self).dispatch(request, *args, **kwargs)



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
        print user
        if user is not None and user.is_active:
            login(request, user)
            return redirect(reverse('get_contactos'))
        else:
            return redirect(reverse('login'))
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


def get_contactos(request):
    user = request.user
    contactos = Person.objects.filter(pk=user.pk)
    return render(
        request,
        'contactos.html',
        {'contactos': contactos}
    )
