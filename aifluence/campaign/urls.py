from django.urls import path
from .views import ActiveCampaigns, campaign_create

urlpatterns = [
    path('active', ActiveCampaigns.as_view(), name='active_campaigns'),
    path('create', campaign_create, name='campaign_create'),
]