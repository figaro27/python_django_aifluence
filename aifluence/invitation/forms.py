from django import forms
from django.forms import TextInput, EmailInput
from django.forms.widgets import Input

from .models import Invitation

class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ['client_id', 'campaign_id', 'influencer_account', 'influencer_platform']