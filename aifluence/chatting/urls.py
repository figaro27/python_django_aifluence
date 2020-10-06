from django.urls import path
from .views import AC, AI, IA

urlpatterns = [
    path('AC', AC, name='AC'),
    path('AI', AI, name='AI'),
    path('IA', IA, name='IA'),
]