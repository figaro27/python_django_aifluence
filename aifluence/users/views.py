from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserCreationForm
from .models import User

def register(request):
    if request.method == 'POST':
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            user = regform.save(commit = False) 
            user.set_password(regform.cleaned_data.get('password2'))
            if (request.POST.get('is_client') == 1):
                user.is_client = True
            else:
                user.is_influencer = True
            user.save()   
    else:
        regform = UserCreationForm()
    return render(request, 'registration/register.html', {'form': regform})