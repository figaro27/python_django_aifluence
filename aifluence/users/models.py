from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE, Model

from django.utils.http import urlencode

class User(AbstractUser):
    
    is_client = models.BooleanField('Client status', default=False)
    is_influencer = models.BooleanField('Influencer status', default=False)

    def __str__(self):
        return self.email


