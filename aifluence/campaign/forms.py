from django import forms
from django.forms import TextInput, EmailInput
from django.forms.widgets import Input

from .models import Campaign

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['brand_name', 'brand_category', 'brand_attributes', 'key_selling_point', 'age_range', \
            'social_status', 'interests', 'personality', 'profession', 'location', 'touchpoint', \
            'campaign_brief', 'campaign_budget'    
        ]