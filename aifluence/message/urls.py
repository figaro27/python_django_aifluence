from django.urls import path
from .views import message_list, create_message, all_channel_messages, read_message, client_message_list, all_campaign_messages, create_client_message

urlpatterns = [
    path('', message_list, name='message_list'),
    path('campaigns', client_message_list, name='client_message_list'),
    path('campaigns/<int:pk>', all_campaign_messages, name='all_campaign_messages'),
    path('campaigns/create', create_client_message, name='create_client_message'),
    path('channels/<int:pk>', all_channel_messages, name='all_channel_messages'),
    path('channels/create', create_message, name='create_message'),
    path('<int:pk>/read', read_message, name='read_message'),
]