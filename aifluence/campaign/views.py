from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db.models.expressions import RawSQL
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q, Count, F, IntegerField
from django.db.models.functions import Cast

from campaign.models import Campaign, Contract, Discussion, Media, Post
from influencer.models import Analysis
from invitation.models import Invitation
from message.models import Message
from users.models import User, Influencer
from .forms import CampaignForm
from dashboard.views import get_num_notification
import aifluence.constants as CONSTANTS
from operator import attrgetter

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
        context.update(get_num_notification(self.request))
        return context
    def get_queryset(self):
        queryset = Campaign.objects.filter(client=self.request.user)
        return queryset
def campaign_view(request, *args, **kwargs):
    if request.method == 'GET':
        campaign_id = kwargs.get('pk')
        post_list = Post.objects.filter(campaign__id=campaign_id, is_posted=True)
        context = dict()
        context = {
            'post_list': post_list,
            'campaign': Campaign.objects.get(pk=campaign_id),
            'menu': 'campaign',
        }
        context.update(get_num_notification(request))
        return render(request, 'campaigns/details.html', context)

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
        context['menu'] = 'campaign'
        context.update(get_num_notification(request))
        return render(request, 'campaigns/create.html', context)
    else:
        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save(commit = False) 
            campaign.client = request.user
            campaign.agent = User.objects.filter(is_staff=True).exclude(is_superuser=True).annotate(Count('agent', distinct=True)).order_by('agent__count').first()
            campaign.save()
        return redirect('active_campaigns')

def campaign_invite_influencers(request, *args, **kwargs):
    if request.method == 'GET':
        campaign_id = kwargs.get('pk')
        campaign = Campaign.objects.get(pk=campaign_id)
        countries = dict(CONSTANTS.COUNTRY_CHOICES)
        socialStatusEarningOptions = dict(CONSTANTS.SOCIAL_STATUS_EARNINGS)

        # Apply filter with campaign information
        influencer_list = Analysis.objects.all()

        #Add invitation status and total followers
        for influencer in influencer_list:
            invitations = influencer.invitation_set.filter(campaign_id=campaign_id, client=request.user)
            if (invitations.count() == 0):
                influencer.invite_status = ""
            else:
                influencer.invite_status = invitations.first().get_status_display
            influencer.followers = influencer.basics['gender']['Male']['number'] + influencer.basics['gender']['Female']['number'] 

            # filter by age range
            influencer.filtered_followers = influencer.followers
            if (len(campaign.age_range) > 0):
                age_filtered_followers = 0
                for age in campaign.age_range:
                    portion = influencer.basics['age'][age[0]]['percent'] / 100 if (age[0] in influencer.basics['age']) > 0 else 0
                    if portion > 0:
                        age_filtered_followers += influencer.filtered_followers * portion
                influencer.filtered_followers = age_filtered_followers

            # filter by interests
            if (len(campaign.interests) > 0):
                interests_filtered_followers = 0
                for interest in campaign.interests:
                    portion = influencer.interests[interest[0]]['percent'] / 100 if (interest[0] in influencer.interests) > 0 else 0
                    if portion > 0:
                        interests_filtered_followers += influencer.filtered_followers * portion
                influencer.filtered_followers = interests_filtered_followers

            # filter by locations
            if (len(campaign.location) > 0):
                locations_filtered_followers = 0
                for location in campaign.location:
                    locationName = countries[location[0]] if (location[0] in countries) else ""
                    portion = influencer.locations[locationName]['percent'] / 100 if (locationName in influencer.locations) > 0 else 0
                    if portion > 0:
                        locations_filtered_followers += influencer.filtered_followers * portion
                influencer.filtered_followers = locations_filtered_followers

            # filter by social status
            if (len(campaign.social_status) > 0):
                social_status_filtered_followers = 0
                for social_status in campaign.social_status:
                    socialStatusEarnings = socialStatusEarningOptions[social_status[0]] if (social_status[0] in socialStatusEarningOptions) else []
                    portion = 0
                    for socialStatusEarning in socialStatusEarnings:
                        portion += influencer.earnings[socialStatusEarning]['percent'] / 100 if (socialStatusEarning in influencer.earnings) > 0 else 0
                    if portion > 0:
                        social_status_filtered_followers += influencer.filtered_followers * portion
                influencer.filtered_followers = int(social_status_filtered_followers)

        influencer_list = sorted(influencer_list, key=attrgetter('filtered_followers'), reverse=True)
        
        context = dict()
        context['menu'] = 'campaign'
        context['object_list'] = influencer_list
        context['campaign_id'] = campaign_id
        context.update(get_num_notification(request))
        return render(request, 'campaigns/invite_influencers.html', context)

#contracts
def contract_list(request, *args, **kwargs):
    if request.method == 'GET':
        if request.user.is_influencer:
            if Influencer.objects.filter(user=request.user).count()==0:
                messages.warning(request, 'You must fill out the profile form to see contracts')
                return redirect('influencer_profile')
            queryset = Contract.objects.filter(discussion__influencer__user=request.user)
        else:
            queryset = Contract.objects.filter(discussion__campaign__agent=request.user)
        context = dict()
        context['menu'] = 'contracts'
        context['contract_list'] = queryset
        context.update(get_num_notification(request))
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
        context.update(get_num_notification(request))
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

def create_discussion(invitation, influencer):

    discussion = Discussion()
    discussion.campaign = invitation.campaign
    discussion.influencer = influencer
    discussion.invitation = invitation
    discussion.influencer_platform = invitation.influencer_platform
    discussion.posting_suggestion = 'Video style'
    discussion.save()

    message = Message()
    message.discussion = discussion
    message.sent_by = invitation.campaign.agent
    message.sent_to = influencer.user
    message.content = discussion.posting_suggestion
    message.save()
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
        message.content = "I have uploaded post media. Please take a look at <a href='#' onclick='see_media_upload(this)' data-id='" + str(contract.id) + "'>here</a> and let me know your thought."
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
            post.campaign = media.contract.discussion.campaign
            post.influencer = media.contract.discussion.influencer
            post.save()

        message = Message()
        message.sent_by = media.contract.discussion.campaign.agent
        message.sent_to = media.contract.discussion.influencer.user
        message.discussion = media.contract.discussion
        message.content = content
        message.save()

        return redirect('/campaigns/contracts/' + str(media.contract.id) + '?post_actived=1')

def post_update(request, *args, **kwargs):
    if request.method == 'POST':
        post = Post.objects.get(pk=request.POST.get('post_id'))
        post.is_posted = True if request.POST.get('post_status') == 'on' else False
        post.url = request.POST.get('post_url')
        post.save()

        return redirect('/campaigns/contracts/' + str(post.media.contract.id) + '?post_actived=1')
