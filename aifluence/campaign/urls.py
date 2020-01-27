from django.urls import path
from .views import ActiveCampaigns, campaign_create, campaign_invite_influencers, ContractListView, InfluencerDiscussions, contract_offer_agreement

urlpatterns = [
    path('active', ActiveCampaigns.as_view(), name='active_campaigns'),
    path('create', campaign_create, name='campaign_create'),
    path('<int:pk>/invite_influencers', campaign_invite_influencers, name='campaign_invite_influencers'),
    path('contracts', ContractListView.as_view(), name='contract_list'),
    path('contracts/offer/<int:pk>/agreement', contract_offer_agreement, name='contract_offer_agreement'),
    path('influencer/discussions', InfluencerDiscussions.as_view(), name='influencer_discussions'),
]