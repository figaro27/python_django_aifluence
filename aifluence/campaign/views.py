from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db.models.expressions import RawSQL

from campaign.models import Campaign, Contract, Discussion
from influencer.models import Analysis
from invitation.models import Invitation
from message.models import Message
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
    def get_queryset(self):
        queryset = Campaign.objects.filter(client=self.request.user)
        return queryset

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
        context['campaign_id'] = campaign_id
        return render(request, 'campaigns/invite_influencers.html', context)

#contracts
class ContractListView(ListView):
    model = Contract
    context_object_name = 'contract_list'

    def get_context_data(self, **kwargs):
        context = super(ContractListView, self).get_context_data(**kwargs)
        context.update({
            'menu':'contracts'
        })
        return context
    
    def get_queryset(self):
        if self.request.user.is_influencer:
            queryset = Contract.objects.filter(discussion__influencer__user=self.request.user)
        else:
            queryset = Contract.objects.filter(discussion__campaign__agent=self.request.user)
        return queryset

    def get_template_names(self):
        if self.request.user.is_influencer:
            return ['campaigns/influencer_contracts.html']
        else:
            return ['campaigns/agent_contracts.html']

def contract_offer_agreement(request, *args, **kwargs):
    if request.method == 'POST':
        contract_id = kwargs.get('pk')
        contract = Contract.objects.get(pk=contract_id)
        agreement = request.POST.get('agreement')
        comment = request.POST.get('comment')
        message_id = request.POST.get('message_id')
        message = Message()
        message.sent_by = contract.discussion.influencer.user
        message.sent_to = contract.discussion.campaign.agent
        message.discussion = contract.discussion

        content = ''
        contract_status = 'AC'
        if (agreement == 0):
            content = "The contract <span class='font-weight-bold'>" + contract.contract_title + "</span> has been declined.<br/>" + comment
            contract_status = 'DE'
        else:
            content = "<span class='text-success'>Congratulations!</span><br/>The contract <span class='font-weight-bold'>" + contract.contract_title + "</span> has been accepted.<br/>" + comment 
        message.content = content
        message.save()

        contract.contract_status = contract_status
        contract.save()

        offer_message = Message.objects.get(pk=message_id)
        offer_message.content = offer_message.content.replace("contract_agree(this)", "")
        offer_message.save()

        return render(request, 'messages/message_body.html', {'channel_messages': Message.objects.filter(discussion=contract.discussion).order_by('sent_at'),})

class InfluencerDiscussions(ListView):
    model = Discussion
    template_name = 'campaigns/influencer_discussions.html'
    context_object_name = 'discussion_list'

    def get_context_data(self, **kwargs):
        context = super(InfluencerDiscussions, self).get_context_data(**kwargs)
        context.update({
            'menu':'discussions'
        })
        return context

    def get_queryset(self):
        queryset = Discussion.objects.filter(influencer__user=self.request.user)
        return queryset

def create_discussion(invitation, influencer):

    discussion = Discussion()
    discussion.campaign = invitation.campaign
    discussion.influencer = influencer
    discussion.invitation = invitation
    discussion.influencer_platform = invitation.influencer_platform
    discussion.posting_suggestion = 'Video style'
    discussion.save()
    return discussion.id

# def offer_contract(reqeust, *args, **kwargs):
