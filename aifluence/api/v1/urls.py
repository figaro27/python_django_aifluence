from django.urls import path
from django.conf.urls import url, include

from rest_framework import routers, viewsets

router = routers.DefaultRouter()
# router.register(r'invitation', invitation_views.InvitationsViewSet)
app_name = "v1"
urlpatterns = [
    path('invitations/', include('api.v1.invitation.urls', namespace='invitation')),
]

urlpatterns +=router.urls

