from rest_framework import serializers
from invitation.models import Invitation
class InvitationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invitation
        fields = ['invitation_content', 'influencer_platform', 'status']