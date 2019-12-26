from rest_framework import routers
from django.urls import path
from . import views

app_name = "invitation"
router = routers.DefaultRouter()
router.register(r'', views.InvitationViewSet)

urlpatterns = [
    path('influencer/<int:pk>', views.InviteInfluencerView.as_view(), name='invite_influencer'),
]

urlpatterns +=router.urls