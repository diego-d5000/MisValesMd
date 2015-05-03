from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.template.context_processors import csrf
from .models import Person, Group
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms as cForms

def home(req):
    if req.user:
        return redirect(reverse('get_contactos'))
    else:
        return render(req,'index.html',{})

class PersonView(View):

    def get(self, req):
        user = req.user
        group = req.GET.get('group')
        contactos = Person.objects.filter(user=user, group=group) if group else Person.objects.filter(user=user)
        groups = Group.objects.filter(user=user)
        form1 = cForms.PersonForm()
        form2 =  cForms.GroupForm()
        return render(req,'contactos.html', locals())

    def post(self, req):
        form = cForms.PersonForm(req.POST)
        print "RQ", req.POST

        if form.is_valid():
            form.save(user=req.user)
            print 'bien'
            return HttpResponse('Se ha guardado el contacto')
        else:
            print 'bien'
            return HttpResponse('Hubo un error, intente mas tarde')

def newGroup(req):
    form = cForms.GroupForm(req.POST)

    if form.is_valid():
        form.save(user=req.user)
        return HttpResponse("Se ha guardado el grupo")
    else:
        return HttpResponse("Hubo un error, intente mas tarde")


class RegisterView(View):
    def get(self, req):
        form = UserCreationForm()
        return render(req, 'register.html', {'form': form})

    def post(self, req):
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
        else:
            return render(req, 'register.html', {'form': form})


class LoginView(View):
    def get(self, req):
        form = AuthenticationForm()
        return render(req, 'login.html', {'form':form})

    def post(self, req):
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(req, user)
            return redirect(reverse('get_contactos'))

def logout_view(req):
    logout(req)
    return redirect(reverse('home'))
