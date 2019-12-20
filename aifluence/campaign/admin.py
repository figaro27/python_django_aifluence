from django.contrib import admin
from .models import Campaign
# Register your models here.
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'brand_category', 'brand_attributes', 'key_selling_point', 'age_range', \
            'social_status', 'interests', 'personality', 'profession', 'location', 'touchpoint', \
            'campaign_brief', 'campaign_budget'    
    )
admin.site.register(Campaign, CampaignAdmin)