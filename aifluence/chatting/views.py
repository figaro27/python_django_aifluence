from django.shortcuts import render

# Create your views here.
import asyncio
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from urllib import request
from django.core.mail import EmailMultiAlternatives, send_mail
from django.db.models import Q, Count
from django.http import HttpResponseNotFound, HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from datetime import date, datetime

from campaign.models import Campaign, Discussion, Contract
from message.models import Message
from users.models import Influencer

from dashboard.views import get_num_notification
from utils.chat import get_dialogs
from aifluence.constants import QB_CONFIG

# Create your views here.

def AC(request, *args, **kwargs):
    chat_session_token = request.session['chat_session_token']
    chat_id = request.session['chat_id']
    return render(
        request,
        'chat/index.html',
        {
            'username': request.session['username'],
            'chat_session_token': chat_session_token,
            'chat_id' : chat_id,
            'type' : QB_CONFIG['chat']['dialog_custom_type']['CA'],
            'menu' : 'AC'
        }
    )

def AI(request, *args, **kwargs):
    chat_session_token = request.session['chat_session_token']
    chat_id = request.session['chat_id']
    return render(
        request,
        'chat/index.html',
        {
            'username': request.session['username'],
            'chat_session_token': chat_session_token,
            'chat_id' : chat_id,
            'type' : QB_CONFIG['chat']['dialog_custom_type']['AI'],
            'menu' : 'AI',
            'from_to' : 'AI'
        }
    )

def IA(request, *args, **kwargs):
    chat_session_token = request.session['chat_session_token']
    chat_id = request.session['chat_id']
    return render(
        request,
        'chat/index.html',
        {
            'username': request.session['username'],
            'chat_session_token': chat_session_token,
            'chat_id' : chat_id,
            'type' : QB_CONFIG['chat']['dialog_custom_type']['AI'],
            'menu' : 'IA',
            'from_to' : 'IA'
        }
    )

