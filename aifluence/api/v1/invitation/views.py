from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from invitation.models import Invitation
from influencer.models import Analysis
from campaign.models import Campaign
from .serializers import InvitationSerializer
from datetime import datetime
from .engine import send_invitation
# Create your views here.

class InvitationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer

class InviteInfluencerView(APIView):
    def post(self, request, format=None, *args, **kwargs):
        influencer_id = kwargs['pk']
        action = request.data['action']
        campaign_id = request.data['campaign_id']
        influencer = Analysis.objects.get(pk=influencer_id)
        campaign = Campaign.objects.get(pk=campaign_id)
        code = ""

        if action=='invite':

            #send invitation in instagram
            try:
                invitations = Invitation.objects.filter(client=request.user, campaign__id=campaign_id, analysis=influencer)

                if invitations.count() > 0:
                    if send_invitation(influencer.influencer_account, influencer.influencer_platform, campaign_id, invitations.first().invitation_key):
                        invitations.update(status='SE', last_sent_at=datetime.now())
                        code = 'success'
                    else:
                        code = 'failed'
                else:
                    invitation = Invitation()
                    invitation.client = request.user
                    invitation.campaign = campaign
                    invitation.influencer_account = influencer.influencer_account
                    invitation.influencer_platform = influencer.influencer_platform
                    invitation.invitation_content = "We invite you to the marketing campaign you'd be interested in."
                    invitation.status = 'CR'
                    invitation.analysis = influencer
                    invitation.save()

                    if send_invitation(influencer.influencer_account, influencer.influencer_platform, campaign_id, invitation.invitation_key):
                        invitation.status = 'SE'
                        invitation.last_sent_at = datetime.now()
                        print('api/v1/invitation/views.py/inviation.last_sent_at+++++++++++++++++++++++++++++++++++++++', invitation.last_sent_at)
                        invitation.save()
                        code = 'success'
                    else:
                        code = 'failed'
            except:
                code = 'failed'

        elif action=="reinvite":
            try:
                if send_invitation(influencer.influencer_account, influencer.influencer_platform, campaign_id, invitation.invitation_key):
                    Invitation.objects.filter(client=request.user, campaign__id=campaign_id, analysis=influencer).update(status='SE')
                    code = 'success'
                else:
                    code = 'failed'
            except:
                code = 'failed'
        else:
            try:
                Invitation.objects.filter(client=request.user, campaign__id=campaign_id, analysis=influencer).update(status='CA')
                code = 'success'
            except:
                code = 'failed'

        if code == 'success':
            return Response(status=status.HTTP_201_CREATED)
        elif code == 'failed':
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)