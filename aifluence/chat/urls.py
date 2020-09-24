from django.urls import path
from .views import AC_chat, AI_chat, IA_chat

urlpatterns = [
    path('AC_chat', AC_chat, name='AC_chat'),
    path('AI_chat', AI_chat, name='AI_chat'),
    path('IA_chat', IA_chat, name='IA_chat'),
]