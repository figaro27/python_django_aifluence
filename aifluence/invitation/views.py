from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.db.models import Q
from datetime import datetime

from .models import Invitation
from users.models import Account
from users.forms import UserCreationForm
# Create your views here.
from .forms import InvitationForm

def invitation_create(request):
    if request.method == 'POST':
        form = InvitationForm(request.POST)
        if form.is_valid():
            invitation = form.save(commit = False) 
            invitation.save()
    else:
        form = InvitationForm()
    return render(request, 'invitation/create.html', {'form': form})

def invitation_influencer(request, invitation_key=None, accepted=None):
    try:
        invitation = Invitation.objects.get(invitation_key=invitation_key)
    except Invitation.DoesNotExist:
        invitation = None
    if invitation:
        if invitation.status == 'EX':
            return HttpResponseNotFound('<h1>Invitation has been expired</h1>')
        if (datetime.now() - invitation.last_sent_at.replace(tzinfo=None)).days > 1:
            invitation.status = 'EX'
            invitation.save()
            return HttpResponseNotFound('<h1>Invitation has been expired</h1>')
        else:
            if request.GET.get('accepted') == 'true': 
                invitation.status = 'AC'
                invitation.save()

                if (invitation.influencer_platform == 'IN'):
                    users = Account.objects.filter(instagram_account=invitation.influencer_account)
                elif (invitation.influencer_platform == 'FA'):
                    users = Account.objects.filter(facebook_account=invitation.influencer_account)
                elif (invitation.influencer_platform == 'TW'):
                    users = Account.objects.filter(twitter_account=invitation.influencer_account)
                else:
                    users = Account.objects.filter(linkedin_account=invitation.influencer_account)

                if (users.count() > 0):
                    login(request, users.first())
                    return redirect('login')
                else:
                    is_invited = True
                    return render(request, 'registration/register.html', {'is_invited': is_invited, 'form': UserCreationForm(), 'invitation': invitation})
            else:
                invitation.status = 'RE'
                invitation.save()
                return HttpResponse()
    else:
        return HttpResponseNotFound('<h1>Error</h1>')