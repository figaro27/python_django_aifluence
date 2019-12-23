from django.db import models
from django.contrib.postgres.fields import JSONField

PLATFORM_CHOICES = (
    ('IN', 'Instagram'),
    ('FA', 'Facebook'),
    ('TW', 'Twitter')
)

# Create your models here.
class Analysis(models.Model):
    # influencer info
    influencer_account = models.CharField(max_length=30)
    influencer_platform = models.CharField(max_length=2, choices=PLATFORM_CHOICES, default='IN')
    # psycographic analysis
    basics = JSONField(null=True)
    earnings = JSONField(null=True)
    interests = JSONField(null=True)
    locations = JSONField(null=True)
    personality_traits = JSONField(null=True)
    engagements = JSONField(null=True)
    # sentiment analysis
    sentiments = JSONField(null=True)
    #
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)