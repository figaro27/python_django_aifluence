from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserCreationForm, InfluencerProfileForm, LoginForm
from .models import User, Influencer
from .auth import EmailOrUsernameModelBackend
from campaign.views import create_discussion
from invitation.models import Invitation

def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            
            user = EmailOrUsernameModelBackend.authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                if request.POST.get('invitation_key'):
                    return redirect('/influencer/profile?invitation_key=' + request.POST.get('invitation_key'))
                if request.POST.get('discussion_id'):
                    return redirect('/campaigns/influencer/discussions/' + request.POST.get('discussion_id'))
                return redirect('dashboard')
            else:
                form.add_error('username', 'error')
    else:
        form = LoginForm()
        if request.GET.get('discussion_id'):
            return render(request, 'registration/login.html', {'form': form, 'discussion_id': request.GET.get('discussion_id')})
        if request.GET.get('invitation_key'):
            return render(request, 'registration/login.html', {'form': form, 'invitation_key': request.GET.get('invitation_key')})
    return render(request, 'registration/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            print('asdfasdfasdf')
            user = regform.save(commit = False) 
            user.set_password(regform.cleaned_data.get('password2'))
            if (request.POST.get('is_client') == "1"):
                user.is_client = True
            else:
                user.is_influencer = True
            user.save()
            if request.POST.get('invitation_key'):
                print(request.POST.get('invitation_key'))
                return redirect('/login?invitation_key=' + request.POST.get('invitation_key'))
            return redirect('custom_login')
    else:
        regform = UserCreationForm()
        if request.GET.get('invitation_key'):
            return render(request, 'registration/register.html', {'form': regform, 'invitation_key': request.GET.get('invitation_key')})
        return render(request, 'registration/register.html', {'form': regform})

def influencer_profile(request):
    try:
        influencer = Influencer.objects.get(user=request.user)
    except Influencer.DoesNotExist:
        influencer = None
        
    if request.method == 'GET':
        profileForm = InfluencerProfileForm(instance=influencer)
        if request.GET.get('invitation_key'):
            messages.warning(request, 'You must fill out the profile form to see invitations')
            return render(request, 'registration/influencer_profile.html', {'form': profileForm, 'menu': 'profile', 'invitation_key': request.GET.get('invitation_key')})
        return render(request, 'registration/influencer_profile.html', {'form': profileForm, 'menu': 'profile'})
    else:
        profileForm = InfluencerProfileForm(request.POST)
        if profileForm.is_valid():
            if influencer == None:
                influencer = profileForm.save(commit=False)
                influencer.user = request.user
                influencer.save()
            else:
                influencer.instagram_account = request.POST.get('instagram_account')
                influencer.facebook_account = request.POST.get('facebook_account')
                influencer.twitter_account = request.POST.get('twitter_account')
                influencer.save()
            if request.POST.get('invitation_key'):
                invitation_key = request.POST.get('invitation_key')
                invitation = Invitation.objects.get(invitation_key=invitation_key)
                discussion_id = create_discussion(invitation, influencer)
                return redirect('/campaigns/influencer/discussions/' + str(discussion_id))
            return redirect('dashboard')