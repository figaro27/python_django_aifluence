from django.contrib import admin

from .models import Invitation
# Register your models here.
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('client', 'campaign', 'invitation_key', 'analysis', 'influencer_platform', 'invitation_content', 'created_at', 'last_sent_at', 'status')
    list_filter = ('influencer_platform', 'status')
    search_fields = ['influencer_account']
    readonly_fields = ('invitation_key', 'created_at')
admin.site.register(Invitation, InvitationAdmin)