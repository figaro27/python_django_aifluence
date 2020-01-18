from django.urls import path
from .views import ActiveCampaigns, campaign_create, campaign_invite_influencers, InfluencerContracts, InfluencerDiscussions

urlpatterns = [
    path('active', ActiveCampaigns.as_view(), name='active_campaigns'),
    path('create', campaign_create, name='campaign_create'),
    path('<int:pk>/invite_influencers', campaign_invite_influencers, name='campaign_invite_influencers'),
    path('influencer/contracts', InfluencerContracts.as_view(), name='influencer_contracts'),
    path('influencer/discussions', InfluencerDiscussions.as_view(), name='influencer_discussions'),
]