from django.urls import path
from .views import messages, create_message, all_channel_messages

urlpatterns = [
    path('', messages, name='messages'),
    path('channels/<int:pk>', all_channel_messages, name='all_channel_messages'),
    path('channels/create', create_message, name='create_message'),
]