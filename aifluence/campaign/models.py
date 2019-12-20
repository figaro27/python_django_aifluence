from django.db import models
from django.db.models import CASCADE

from users.models import User
# Create your models here.
class Campaign(models.Model):
    #Brand
    brand_name = models.CharField(null=True, blank=True, max_length=255)
    brand_category = models.CharField(null=True, blank=True, max_length=255)
    brand_comptetitors = models.CharField(null=True, blank=True, max_length=255)
    brand_attributes = models.CharField(null=True, blank=True, max_length=255)
    key_selling_point = models.CharField(null=True, blank=True, max_length=255)

    #Consumer
    age_range = models.CharField(null=True, blank=True, max_length=255)
    social_status = models.CharField(null=True, blank=True, max_length=255)
    interests = models.CharField(null=True, blank=True, max_length=255)
    personality = models.CharField(null=True, blank=True, max_length=255)
    profession = models.CharField(null=True, blank=True, max_length=255)
    location = models.CharField(null=True, blank=True, max_length=255)
    touchpoint = models.CharField(null=True, blank=True, max_length=255)

    #campaign
    campaign_brief = models.TextField(null=True, blank=True, max_length=4000)
    campaign_budget = models.IntegerField()
    campaign_currency = models.CharField(max_length=20, null=True, blank=True)
    campaign_kpis = models.CharField(max_length=64, null=True, blank=True)
    active_social_media = models.CharField(max_length=64, null=True, blank=True)
    previous_marketing_campaigns = models.CharField(max_length=64, null=True, blank=True)
    owned_event = models.CharField(max_length=64, null=True, blank=True)
    sponsored_event = models.CharField(max_length=64, null=True, blank=True)
    client = models.ForeignKey(User, on_delete=CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)