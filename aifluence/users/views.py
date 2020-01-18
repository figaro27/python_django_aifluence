from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserCreationForm, InfluencerProfileForm, LoginForm
from .models import User, Influencer
from .auth import EmailOrUsernameModelBackend

def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            
            user = EmailOrUsernameModelBackend.authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error('username', 'error')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            user = regform.save(commit = False) 
            user.set_password(regform.cleaned_data.get('password2'))
            if (request.POST.get('is_client') == "1"):
                user.is_client = True
            else:
                user.is_influencer = True
            user.save()
            if request.POST.get('invitation_id'):
                return render(request, 'registration/login.html', {'invitation_id': request.POST.get('invitation_id')})
            return redirect('login')
    else:
        regform = UserCreationForm()
        return render(request, 'registration/register.html', {'form': regform})

def influencer_profile(request):
    try:
        influencer = Influencer.objects.get(user=request.user)
    except Influencer.DoesNotExist:
        influencer = None
        
    if request.method == 'GET':
        profileForm = InfluencerProfileForm(instance=influencer)
        return render(request, 'registration/influencer_profile.html', {'form': profileForm, 'menu': 'profile'})
    else:
        profileForm = InfluencerProfileForm(request.POST)
        if profileForm.is_valid():
            if influencer == None:
                profile = profileForm.save(commit=False)
                profile.user = request.user
                profile.save()
            else:
                influencer.instagram_account = request.POST.get('instagram_account')
                influencer.facebook_account = request.POST.get('facebook_account')
                influencer.twitter_account = request.POST.get('twitter_account')
                influencer.save()
            return redirect('dashboard')