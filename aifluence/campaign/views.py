from django.shortcuts import render
from django.views.generic import ListView

from .models import Campaign
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
        return context