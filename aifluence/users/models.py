import hashlib
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE, Model

from django.utils.http import urlencode

class User(AbstractUser):
    
    is_client = models.BooleanField('Client status', default=False)
    is_influencer = models.BooleanField('Influencer status', default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Influencer(models.Model):

    user = models.ForeignKey(User, on_delete=CASCADE)
    instagram_account = models.CharField(max_length=60, null=True, blank=True)
    facebook_account = models.CharField(max_length=60, null=True, blank=True)
    twitter_account = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
