from django.urls import path
from .views import ActiveCampaigns, campaign_create, campaign_invite_influencers, ContractListView, InfluencerDiscussions, contract_offer_agreement, contract_view, \
    media_create, media_agreement

urlpatterns = [
    path('active', ActiveCampaigns.as_view(), name='active_campaigns'),
    path('create', campaign_create, name='campaign_create'),
    path('<int:pk>/invite_influencers', campaign_invite_influencers, name='campaign_invite_influencers'),
    path('contracts', ContractListView.as_view(), name='contract_list'),
    path('contracts/<int:pk>', contract_view, name='contract_view'),
    path('contracts/offer/<int:pk>/agreement', contract_offer_agreement, name='contract_offer_agreement'),
    path('influencer/discussions', InfluencerDiscussions.as_view(), name='influencer_discussions'),
    path('contracts/<int:pk>/media/create', media_create, name='media_create'),
    path('contracts/media/<int:pk>/agreement', media_agreement, name='media_agreement'),
]