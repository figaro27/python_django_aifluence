from django.urls import path
from .views import invitation_create, invitation_influencer, invitation_accepted, invitation_rejected

urlpatterns = [
    path('create', invitation_create, name='invitation_create'),
    path(r'<invitation_key>', invitation_influencer, name='invitation_influencer'),
    path(r'<invitation_key>/accepted', invitation_accepted, name='invitation_accepted'),
    path(r'<invitation_key>/rejected', invitation_rejected, name='invitation_rejected'),
]