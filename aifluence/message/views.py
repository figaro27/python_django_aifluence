from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from urllib import request
from django.core.mail import EmailMultiAlternatives, send_mail
from django.db.models import Q
from django.http import HttpResponseNotFound, HttpResponse, JsonResponse
from datetime import date, datetime

from campaign.models import Discussion
from message.models import Message
# Create your views here.

def messages(request, *args, **kwargs):
    if request.method == 'GET':
        agents = []
        if request.user.is_influencer:
            discussions = Discussion.objects.filter(influencer__user=request.user)
        if request.user.is_staff:
            discussions = Discussion.objects.filter(campaign__agent=request.user)
        return render(request, 'messages/index.html', {'menu': 'messages', 'discussions': discussions,})