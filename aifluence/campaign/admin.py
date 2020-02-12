from django.contrib import admin
from .models import Campaign, Discussion, Contract, Post, Media
# Register your models here.
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'brand_category', 'brand_attributes', 'key_selling_point', 'age_range', \
            'social_status', 'interests', 'personality', 'profession', 'location', 'touchpoint', \
            'campaign_brief', 'campaign_budget'    
    )
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'invitation', 'influencer', 'influencer_platform', 'posting_suggestion', 'created_at', 'updated_at')
    
class ContractAdmin(admin.ModelAdmin):
    list_display = ('discussion', 'contract_title', 'contract_terms', 'contract_status', 'contract_budget', 'created_at', 'updated_at')

class MediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_name', 'upload_by', 'media', 'contract', 'status', 'created_at')

class PostAdmin(admin.ModelAdmin):
    list_display = ('media', 'is_posted', 'url', 'analysis', 'post_date', 'campaign', 'influencer', 'created_at','updated_at')

admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Discussion, DiscussionAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Post, PostAdmin)