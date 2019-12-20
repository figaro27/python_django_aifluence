from django.urls import path
from .views import ActiveCampaigns

urlpatterns = [
    path('active', ActiveCampaigns.as_view(), name='active_campaigns'),
]