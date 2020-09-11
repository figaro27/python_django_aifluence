from django.urls import path
from .views import CA_chat, AI_chat

urlpatterns = [
    path('CA_chat', CA_chat, name='CA_chat'),
    path('AC_chat', CA_chat, name='AC_chat'),
    path('AI_chat', AI_chat, name='AI_chat'),
]