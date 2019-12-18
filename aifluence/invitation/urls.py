from django.urls import path
from .views import invitation_create, invitation_influencer

urlpatterns = [
    path('create', invitation_create, name='invitation_create'),
    path(r'<invitation_key>', invitation_influencer, name='invitation_influencer')
]