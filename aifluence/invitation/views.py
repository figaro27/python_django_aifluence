from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.db.models import Q
from django.views.generic import ListView
from datetime import datetime

from .models import Invitation
from users.models import Influencer
from users.forms import UserCreationForm
# Create your views here.
from .forms import InvitationForm

def influencer_invitations(request):
    print('asdfasd')
    if request.method == 'GET':
        try:
            influencer = Influencer.objects.get(user=request.user)
            invitation_list = Invitation.objects.filter(Q(influencer_account=influencer.instagram_account)|Q(influencer_account=influencer.facebook_account)|Q(influencer_account=influencer.twitter_account))
        except Influencer.DoesNotExist:
            messages.warning(request, 'You must fill the profile form to see invitations')
            return HttpResponseRedirect(reverse('dashboard'))

        context = dict()
        context.update({
            'menu':'invitations',
            'invitation_list': invitation_list
        })
        return render(request, 'invitation/influencer_invitations.html', context)

def invitation_create(request):
    if request.method == 'POST':
        form = InvitationForm(request.POST)
        if form.is_valid():
            invitation = form.save(commit = False) 
            invitation.save()
    else:
        form = InvitationForm()
    return render(request, 'invitation/create.html', {'form': form})

def invitation_influencer(request, invitation_key=None):
    try:
        invitation = Invitation.objects.get(invitation_key=invitation_key)
    except Invitation.DoesNotExist:
        invitation = None
    if invitation:
        if invitation.status == 'CA':
            return HttpResponseNotFound('<h1>Invitation has been canceled</h1>')
        
        if (invitation.status == 'EX') or (invitation.last_sent_at and (datetime.now() - invitation.last_sent_at.replace(tzinfo=None)).days > 1):
            invitation.status = 'EX'
            invitation.save()
            return HttpResponseNotFound('<h1>Invitation has been expired</h1>')
        else:
            return render(request, 'invitation/campaign_info.html', {'invitation': invitation})
    else:
        return HttpResponseNotFound('<h1>Error</h1>')

def invitation_accepted(request, invitation_key=None):
    try:
        invitation = Invitation.objects.get(invitation_key=invitation_key)
    except Invitation.DoesNotExist:
        invitation = None
    if invitation:
        invitation.status = 'AC'
        invitation.save()

        if (invitation.influencer_platform == 'IN'):
            users = Influencer.objects.filter(instagram_account=invitation.influencer_account)
        elif (invitation.influencer_platform == 'FA'):
            users = Influencer.objects.filter(facebook_account=invitation.influencer_account)
        elif (invitation.influencer_platform == 'TW'):
            users = Influencer.objects.filter(twitter_account=invitation.influencer_account)
        else:
            users = Influencer.objects.filter(linkedin_account=invitation.influencer_account)

        if (users.count() > 0):
            login(request, users.first())
            return redirect('dashboard')
        else:
            is_invited = True
            return render(request, 'registration/register.html', {'is_invited': is_invited, 'form': UserCreationForm(), 'invitation': invitation})
    else:
        return HttpResponseNotFound('<h1>Error</h1>')

def invitation_rejected(request, invitation_key=None):
    try:
        invitation = Invitation.objects.get(invitation_key=invitation_key)
    except Invitation.DoesNotExist:
        invitation = None
    if invitation:
        invitation.status = 'RE'
        invitation.save()
        return HttpResponseNotFound('<h1>Invitation has been rejected</h1>')
    else:
        return HttpResponseNotFound('<h1>Error</h1>')