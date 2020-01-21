from django.urls import path
from .views import messages

urlpatterns = [
    path('', messages, name='messages'),
]