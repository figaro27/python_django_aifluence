from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from users.models import Influencer
# Create your views here.
@login_required
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
        return render(request, 'home/home_influencer.html', context)
    elif request.user.is_client:
        return render(request, 'home/home_client.html', context)
    elif request.user.is_staff:
        return render(request, 'home/home_agent.html', context)
    