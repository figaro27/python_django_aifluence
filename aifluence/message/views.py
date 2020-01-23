from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from urllib import request
from django.core.mail import EmailMultiAlternatives, send_mail
from django.db.models import Q
from django.http import HttpResponseNotFound, HttpResponse, JsonResponse
from datetime import date, datetime

from campaign.models import Discussion, Contract
from message.models import Message
# Create your views here.

def messages(request, *args, **kwargs):
    if request.method == 'GET':
        if request.user.is_influencer:
            discussions = Discussion.objects.filter(influencer__user=request.user)
        if request.user.is_staff:
            discussions = Discussion.objects.filter(campaign__agent=request.user)
        if request.GET.get('invited') == 'true':
            discussion_id = request.GET.get('id')
            return render(request, 'messages/index.html', {'menu': 'messages', 'discussions': discussions, 'discussion_id': discussion_id,})
        return render(request, 'messages/index.html', {'menu': 'messages', 'discussions': discussions,})

def create_message(request, *args, **kwargs):
    if request.method == 'POST':
        discussion_id = request.POST.get('discussion_id')
        discussion = Discussion.objects.get(pk=discussion_id)
        content = request.POST.get('content')
        type = request.POST.get('type')
        
        message = Message()
        if type == 'IA':
            message.sent_by = discussion.influencer.user
            message.sent_to = discussion.campaign.agent
        if type == 'AI' or type == 'CO':
            message.sent_by = discussion.campaign.agent
            message.sent_to = discussion.influencer.user

        message.discussion = discussion
        message.content = content
        message.save()

        if type == 'CO':
            budget = request.POST.get('budget')
            contract = Contract()
            contract.contract_terms = request.POST.get('terms')
            contract.contract_status = 'OF'
            contract.contract_budget = budget
            contract.discussion = discussion
            contract.save()
            
        return render(request, 'messages/message_body.html', {'channel_messages': Message.objects.filter(discussion__id=discussion_id),})

def all_channel_messages(request, *args, **kwargs):
    channel_messages = Message.objects.filter(discussion__id=kwargs.get('pk'))
    discussion = Discussion.objects.get(pk=kwargs.get('pk'))
        
    return render(request, 'messages/channel.html', {'channel_messages': channel_messages, 'discussion_id': kwargs.get('pk'), 'description': discussion})
