from django.urls import path
from .views import message_list, create_message, all_channel_messages, read_message

urlpatterns = [
    path('', message_list, name='message_list'),
    path('channels/<int:pk>', all_channel_messages, name='all_channel_messages'),
    path('channels/create', create_message, name='create_message'),
    path('<int:pk>/read', read_message, name='read_message'),
]