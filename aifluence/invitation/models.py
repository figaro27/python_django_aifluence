from django.db import models
from django.utils.crypto import get_random_string
# Create your models here.
from django.db.models import CASCADE
from django.urls import reverse
from aifluence.constants import PLATFORM_CHOICES
from users.models import User
from campaign.models import Campaign
from influencer.models import Analysis
import uuid

INVITATION_STATUS = (
    ('CR', 'CREATED'),
    ('SE', 'SENT'),
    ('AC', 'ACCEPTED'),
    ('RE', 'REJECTED'),
    ('CO', 'COMPLETED'),
    ('EX', 'EXPIRED')
)

def generate_token():
    secret = str(uuid.uuid4()) + str(uuid.uuid4())
    return secret.replace('-', '')[:64]
    
class Invitation(models.Model):
    client = models.ForeignKey(User, on_delete=CASCADE, null=True)
    campaign = models.ForeignKey(Campaign, on_delete=CASCADE, null=True)
    invitation_key = models.CharField(max_length=64, default=generate_token)
    influencer_platform = models.CharField(max_length=2, choices=PLATFORM_CHOICES, default='IN')
    invitation_content = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    last_sent_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=2, choices=INVITATION_STATUS, default='CR')
    analysis = models.ForeignKey(Analysis, on_delete=CASCADE, null=True)
