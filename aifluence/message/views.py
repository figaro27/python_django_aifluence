from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from urllib import request
from django.core.mail import EmailMultiAlternatives, send_mail
from django.db.models import Q, Count
from django.http import HttpResponseNotFound, HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from datetime import date, datetime

from campaign.models import Discussion, Contract
from message.models import Message
from users.models import Influencer

from dashboard.views import get_num_notification
# Create your views here.

def message_list(request, *args, **kwargs):
    if request.method == 'GET':
        context = dict()
        if request.user.is_influencer:
            if Influencer.objects.filter(user=request.user).count() == 0:
                messages.warning(request, 'You must fill out the profile form to see discussions')
                return redirect('influencer_profile')
            discussions = Discussion.objects.filter(influencer__user=request.user).annotate(
                message_count=Count(
                    'message', 
                    filter=Q(message__read_status=False, message__sent_to=request.user),
                    distinct=True
                    )
                )
        if request.user.is_staff:
            discussions = Discussion.objects.filter(campaign__agent=request.user).annotate(
                message_count=Count(
                    'message', 
                    filter=Q(message__read_status=False, message__sent_to=request.user),
                    distinct=True
                    )
                )
        context = { 
            'discussions': discussions,
            'menu': 'messages'
        }

        context.update(get_num_notification(request))
        if request.GET.get('invited') == 'true':
            discussion_id = request.GET.get('id')
            context.update({'discussion_id': discussion_id})
            return render(request, 'messages/index.html', context)
        return render(request, 'messages/index.html', context)

def create_message(request, *args, **kwargs):
    if request.method == 'POST':
        discussion_id = request.POST.get('discussion_id')
        discussion = Discussion.objects.get(pk=discussion_id)
        content = request.POST.get('content')
        type = request.POST.get('type')

        if type == 'CO':
            budget = request.POST.get('budget')
            contract = Contract()
            contract.contract_title = request.POST.get('title')
            contract.contract_terms = request.POST.get('terms')
            contract.contract_status = 'OF'
            contract.contract_budget = budget
            contract.discussion = discussion
            contract.save()
            content = content + "<br/>You can accept or decline this offer <a href='#' onclick='contract_agree(this)' data-id='" + str(contract.id) + "'>here</a>!"
            
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

        return render(request, 'messages/message_body.html', {'channel_messages': Message.objects.filter(discussion__id=discussion_id).order_by('sent_at'),})

def all_channel_messages(request, *args, **kwargs):
    channel_messages = Message.objects.filter(discussion__id=kwargs.get('pk')).order_by('sent_at')
    discussion = Discussion.objects.get(pk=kwargs.get('pk'))
        
    return render(request, 'messages/channel.html', {'channel_messages': channel_messages, 'discussion_id': kwargs.get('pk'), 'description': discussion})

def read_message(request, *args, **kwargs):
    if request.method == 'POST':
        Message.objects.filter(pk=kwargs.get('pk')).update(read_status=True)
        return JsonResponse({})
