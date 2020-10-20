from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from users.models import Influencer
from campaign.models import Contract
from invitation.models import Invitation
from message.models import Message
# Create your views here.
@login_required(login_url='/login')
def dashboard(request):
    if request.user.is_influencer:
        influencer_profiles = Influencer.objects.filter(user=request.user)
        if influencer_profiles.count() == 0:
            messages.warning(request, 'You must fill out the profile form to see home page.')
            return redirect('influencer_profile')
        else:
            if not influencer_profiles.first().instagram_account and not influencer_profiles.first().facebook_account and not influencer_profiles.first().twitter_account:
                return redirect('influencer_profile')

    context = {
        'menu': 'home'
    }

    if request.user.is_influencer:
        context.update(get_num_notification(request))
        return render(request, 'home/home_influencer.html', context)
    elif request.user.is_client:
        context.update(get_num_notification(request))
        return render(request, 'home/home_client.html', context)
    elif request.user.is_staff:
        context.update(get_num_notification(request))
        return render(request, 'home/home_agent.html', context)

def get_num_notification(request):
    context = dict()
    if not request.user.is_client:
        context = {
            'numOfInfluencerMessage': Message.objects.filter(sent_to=request.user,read_status=False,campaign__isnull=True).count()
        }
    if not request.user.is_influencer:
        context.update({'numOfClientMessage': Message.objects.filter(sent_to=request.user,read_status=False,discussion__isnull=True).count()})
    return context
