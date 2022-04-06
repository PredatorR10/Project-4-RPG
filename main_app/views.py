from pyexpat import model
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views import View
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Character
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('HEY', user.username)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            HttpResponse('<h1>Try Again</h1>')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/character_select/'+u)
            else:
                print('The account has been disabled')
        else:
            print('The username and/or password is incorect.')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

@login_required
def charSel(request, username):
    user = User.objects.get(username=username)
    characters = Character.objects.filter(user=user)
    return render(request, 'character_select.html', {'username': username, 'characters': characters})

@method_decorator(login_required, name='dispatch')
class CharCreation(CreateView):
    model = Character
    fields = ['name', 'charClass']
    template_name = "character_create.html"
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/character_select/'+self.object.user.username)