from django.db import models
from django.db.models import CASCADE
from django.contrib.postgres.fields import ArrayField, JSONField

from aifluence.constants import USER_TYPE_CHOICES
from campaign.models import Discussion, Campaign
from users.models import User
# Create your models here.

class Message(models.Model):
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_by')
    sent_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_to')
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, null=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=4000, null=True, blank=True)
    read_status = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)
