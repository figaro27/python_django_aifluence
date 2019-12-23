from django import forms
from django.forms.widgets import Input
from crispy_forms.helper import FormHelper
from .models import Campaign

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['brand_name', 'brand_category', 'brand_attributes', 'key_selling_point', 'brand_comptetitors', 'age_range', \
            'social_status', 'interests', 'personality', 'profession', 'location', 'touchpoint', \
            'campaign_brief', 'campaign_budget', 'campaign_currency', 'campaign_kpis', 'active_social_media', 'previous_marketing_campaigns', 'owned_event', 'sponsored_event'  
        ]
        widgets = {
            'brand_attributes': forms.Textarea(attrs={'rows':5, 'cols':40}),
            'key_selling_point': forms.Textarea(attrs={'rows':5, 'cols':40}),
            'campaign_brief': forms.Textarea(attrs={'rows':5, 'cols':40}),
            'campaign_kpis': forms.Textarea(attrs={'rows':5, 'cols':40})
        }
    def __init__(self, *args, **kwargs):
        super(CampaignForm, self).__init__(*args, **kwargs)
        self.fields['touchpoint'].required = False
        self.fields['brand_comptetitors'].required = False
        self.fields['active_social_media'].required = False
        self.fields['previous_marketing_campaigns'].required = False
        self.fields['owned_event'].required = False
        self.fields['sponsored_event'].required = False
        self.fields['age_range'].required = False
        self.fields['social_status'].required = False
        self.fields['location'].required = False