from django.conf import settings
from django.db.models import Q
from .models import User

class EmailOrUsernameModelBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, username):
        try:
            return User.objects.get(pk=username)
        except User.DoesNotExist:
            return None