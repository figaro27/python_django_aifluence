from django.urls import path
from .views import dp_import

urlpatterns = [
    path('dpimport', dp_import, name='dp_import')
]