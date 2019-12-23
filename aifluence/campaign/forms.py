from django import forms
from django.forms.widgets import Input
from crispy_forms.helper import FormHelper
from .models import Campaign

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['brand_name', 'brand_category', 'brand_attributes', 'key_selling_point', 'age_range', \
            'social_status', 'interests', 'personality', 'profession', 'location', 'touchpoint', \
            'campaign_brief', 'campaign_budget', 'campaign_currency', 'campaign_kpis', 'active_social_media', 'previous_marketing_campaigns', 'owned_event', 'sponsored_event'  
        ]