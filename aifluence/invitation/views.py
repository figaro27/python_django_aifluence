from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.db.models import Q
from django.views.generic import ListView
from datetime import datetime
import asyncio

from .models import Invitation
from users.models import Influencer
from users.forms import UserCreationForm
from campaign.views import create_discussion
from utils.chat import create_dialog, send_first_message
import aifluence.constants as CONSTANTS
# Create your views here.
from .forms import InvitationForm

def influencer_invitations(request):
    if request.method == 'GET':
        try:
            influencer = Influencer.objects.get(user=request.user)
            invitation_list = Invitation.objects.filter(Q(influencer_account=influencer.instagram_account)|Q(influencer_account=influencer.facebook_account)|Q(influencer_account=influencer.twitter_account))
        except Influencer.DoesNotExist:
            messages.warning(request, 'You must fill out the profile form to see invitations')
            return redirect('influencer_profile')

        context = dict()
        context.update({
            'menu':'invitations',
            'invitation_list': invitation_list
        })
        return render(request, 'invitation/index.html', context)

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
        else:
            users = Influencer.objects.filter(twitter_account=invitation.influencer_account)

        if (users.count() > 0):
            discussion_id = create_discussion(invitation, users.first())
            # QB create group dialog of agent and influencer
            dialog_name = request.session['username'] + '__' + invitation.campaign.agent.username + '__' + str(invitation.campaign.id)
            cam_brand_category = ''
            for category in invitation.campaign.brand_category:
                cam_brand_category = cam_brand_category + category[0] + ' '
            cam_location = ''
            for location in invitation.campaign.location:
                cam_location = cam_location + location + ' '
            campaign_detail = '<span class=\'campaign_detail_key\'>Brand Name: </span>' + invitation.campaign.brand_name + '<br><span class=\'campaign_detail_key\'>Brand Category: </span>' + cam_brand_category + '<br><span class=\'campaign_detail_key\'>Brand Attributes: </span>' + invitation.campaign.brand_attributes + '<br><span class=\'campaign_detail_key\'>Key Selling Point: </span>' + invitation.campaign.key_selling_point + '<br><span class=\'campaign_detail_key\'>Brief: </span>' + invitation.campaign.campaign_brief + '<br><span class=\'campaign_detail_key\'>Location: </span>' + cam_location + '<br><span class=\'campaign_detail_key\'>Budget: </span>' + str(invitation.campaign.campaign_budget)

            dialog = asyncio.run(create_dialog(request.session['chat_session_token'],
                dialog_name, request.session['username'],
                invitation.campaign.agent.chat_id,
                CONSTANTS.QB_CONFIG['chat']['dialog_custom_type']['AI'],
                invitation.campaign.id, invitation.campaign.campaign_brief, campaign_detail, discussion_id))

            send_first_message(invitation.campaign.agent.chat_id, dialog['_id'], "Thanks for your accept")

            if request.user.is_authenticated:
                return redirect('/chat/IA_chat')
            else:
                return redirect('/login?discussion_id='+str(discussion_id))

        else:
            return redirect('/login?invitation_key='+invitation.invitation_key)
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