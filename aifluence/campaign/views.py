from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db.models.expressions import RawSQL
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q

from campaign.models import Campaign, Contract, Discussion, Media, Post
from influencer.models import Analysis
from invitation.models import Invitation
from message.models import Message
from users.models import Influencer
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
def contract_list(request, *args, **kwargs):
    if request.method == 'GET':
        if request.user.is_influencer:
            if Influencer.objects.filter(user=request.user).count()==0:
                messages.warning(request, 'You must fill out the profile form to see contracts')
                return HttpResponseRedirect(reverse('dashboard'))
            queryset = Contract.objects.filter(discussion__influencer__user=request.user)
        else:
            queryset = Contract.objects.filter(discussion__campaign__agent=request.user)
        context = dict()
        context['menu'] = 'contracts'
        context['contract_list'] = queryset
        return render(request, 'campaigns/contracts/contract_index.html', context)

def contract_view(request, *args, **kwargs):
    if request.method == 'GET':
        contract_id = kwargs.get('pk')
        contract = Contract.objects.get(pk=contract_id)
        post_actived = True
        if (request.GET.get('post_actived') == '0'):
            post_actived = False
        
        context = {
            'menu': 'contracts', 
            'contract': contract, 
            'media_list': Media.objects.filter(contract=contract).order_by('created_at'), 
            'post_list': Post.objects.filter(media__contract=contract).order_by('post_date'),  
            'post_actived': post_actived,
        }

        return render(request, 'campaigns/contracts/contract_view.html', context)

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

def media_create(request, *args, **kwargs):
    if request.method == 'POST':
        contract_id = kwargs.get('pk')
        contract = Contract.objects.get(pk=contract_id)
        media = Media()
        media.title = request.POST.get('media_title')
        media.media = request.FILES['media_file']
        media.file_name = request.FILES['media_file'].name
        media.upload_by = Influencer.objects.get(user=request.user)
        media.contract = contract
        media.save()

        message = Message()
        message.sent_by = contract.discussion.influencer.user
        message.sent_to = contract.discussion.campaign.agent
        message.discussion = contract.discussion
        message.content = "I have uploaded post media. Please take a look and let me know your thought."
        message.save()

        return redirect('/campaigns/contracts/' + str(contract_id) + '?post_actived=0')

def media_agreement(request, *args, **kwargs):
    if request.method == 'GET':
        media_id = kwargs.get('pk')
        media = Media.objects.get(pk=media_id)
        agreement = request.GET.get('accepted')
        content = ''
        if agreement == 'true':
            media.status = 'AC'
            content = "Your post <span class='font-weight-bold'>" + media.title + "</span> has been accepted. Please post and let me know the post url."
        else:
            media.status = 'DE'
            content = "Your post <span class='font-weight-bold'>" + media.title + "</span> has been declined."
        media.save()

        if agreement == 'true':
            post = Post()
            post.media = media
            post.save()

        message = Message()
        message.sent_by = media.contract.discussion.campaign.agent
        message.sent_to = media.contract.discussion.influencer.user
        message.discussion = media.contract.discussion
        message.content = content
        message.save()

        return redirect('/campaigns/contracts/' + str(media.contract.id) + '?post_actived=0')

def post_update(request, *args, **kwargs):
    if request.method == 'POST':
        post = Post.objects.get(pk=request.POST.get('post_id'))
        post.is_posted = True if request.POST.get('post_status') == 'on' else False
        post.url = request.POST.get('post_url')
        post.save()

        return redirect('/campaigns/contracts/' + str(post.media.contract.id) + '?post_actived=1')
