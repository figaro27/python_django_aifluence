from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db.models.expressions import RawSQL
from django.db.models import F, Sum

from campaign.models import Campaign
from influencer.models import Analysis
from invitation.models import Invitation
from .forms import CampaignForm
import aifluence.constants as CONSTANTS

# Create your views here.
class ActiveCampaigns(ListView):
    model = Campaign
    template_name = 'campaigns/main.html'
    context_object_name = 'campaigns'

    def get_context_data(self, **kwargs):
        context = super(ActiveCampaigns, self).get_context_data(**kwargs)
        context.update({
            'menu':'campaign'
        })
        return context

def campaign_create(request):
    if request.method == 'GET':
        form = CampaignForm()
        context = dict()
        context['form'] = form
        context['brand_categories'] = CONSTANTS.BRAND_CATEGORY_CHOICES
        context['age_ranges'] = CONSTANTS.AGE_RANGE_CHOICES
        context['social_statuses'] = CONSTANTS.SOCIAL_STATUS_CHOICES
        context['interests'] = CONSTANTS.INTERESTS_CHOICES        
        context['countries'] = CONSTANTS.COUNTRY_CHOICES
        return render(request, 'campaigns/create.html', context)
    else:
        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save(commit = False) 
            campaign.client = request.user
            campaign.save()
        return redirect('active_campaigns')

def campaign_invite_influencers(request, *args, **kwargs):
    if request.method == 'GET':
        campaign_id = kwargs.get('pk')
        
        # Apply filter with campaign information
        influencer_list = Analysis.objects.all()

        # Total followers
        influencer_list = influencer_list.annotate(
            number1=RawSQL("basics->'gender'->'Male'->'number'", []),
            number2=RawSQL("basics->'gender'->'Female'->'number'", [])
        ).order_by('-number1', '-number2')

        #Add invitation status and total followers
        for influencer in influencer_list:
            invitations = influencer.invitation_set.filter(campaign_id=campaign_id, client=request.user)
            if (invitations.count() == 0):
                influencer.invite_status = ""
            else:
                influencer.invite_status = invitations.first().get_status_display
            influencer.followers = influencer.basics['gender']['Male']['number'] + influencer.basics['gender']['Female']['number'] 
        
        context = dict()
        context['menu'] = 'campaign'
        context['object_list'] = influencer_list
        return render(request, 'campaigns/invite_influencers.html', context)