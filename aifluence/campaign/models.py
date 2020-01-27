from django.db import models
from django.db.models import CASCADE
from django.contrib.postgres.fields import ArrayField, JSONField

from users.models import User, Influencer
import aifluence.constants as CONSTANTS
# Create your models here.
class Campaign(models.Model):
    #Brand
    brand_name = models.CharField(max_length=255)
    brand_category = ArrayField(
        ArrayField(
            models.CharField(max_length=255, blank=True),
        )
    )
    brand_comptetitors = models.CharField(max_length=255)
    brand_attributes = models.TextField(max_length=2000)
    key_selling_point = models.TextField(max_length=2000)

    #Consumer
    age_range = ArrayField(
        ArrayField(
            models.CharField(max_length=50, blank=True),
        )
    )
    social_status = ArrayField(
        ArrayField(
            models.CharField(max_length=20, blank=True),
        )
    )
    interests = ArrayField(
        ArrayField(
            models.CharField(max_length=30, blank=True),
        )
    )
    personality = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    location = ArrayField(
        ArrayField(
            models.CharField(max_length=30, blank=True),
        )
    )
    touchpoint = models.CharField(max_length=255, null=True, blank=True)

    #campaign
    campaign_brief = models.TextField(max_length=2000)
    campaign_budget = models.IntegerField()
    campaign_currency = models.CharField(max_length=3, choices=CONSTANTS.CURRENCY_CHOICES, default="usd")
    campaign_kpis = models.TextField(max_length=2000)
    active_social_media = models.CharField(max_length=64)
    previous_marketing_campaigns = models.CharField(max_length=64)
    owned_event = models.CharField(max_length=64)
    sponsored_event = models.CharField(max_length=64)
    client = models.ForeignKey(User, on_delete=CASCADE, null=True, related_name='client')
    agent = models.ForeignKey(User, on_delete=CASCADE, null=True, related_name='agent')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand_name

class Discussion(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=CASCADE, null=True)
    invitation = models.ForeignKey('invitation.Invitation', on_delete=CASCADE, null=True)
    influencer = models.ForeignKey(Influencer, on_delete=CASCADE, null=True)
    influencer_platform = models.CharField(max_length=2, choices=CONSTANTS.PLATFORM_CHOICES, default='IN')
    posting_suggestion = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Contract(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=CASCADE, null=True)
    contract_title = models.CharField(max_length=255, blank=True, null=True)
    contract_terms = JSONField(null=True)
    contract_status = models.CharField(max_length=2, choices=CONSTANTS.CONTRACT_STATUS_CHOICES, default='OF')
    contract_budget = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.discussion.campaign + " - " + self.discussion.campaign.client + " - " + self.discussion.influencer
