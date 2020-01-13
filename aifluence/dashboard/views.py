from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import Influencer
# Create your views here.
@login_required
def dashboard(request):
    if request.user.is_influencer:
        influencer_profiles = Influencer.objects.filter(user=request.user)
        if influencer_profiles.count() == 0:
            return redirect('influencer_profile')
        else:
            if not influencer_profiles.first().instagram_account and not influencer_profiles.first().facebook_account and not influencer_profiles.first().twitter_account:
                return redirect('influencer_profile')
    return render(request, 'layouts/dashboard.html')