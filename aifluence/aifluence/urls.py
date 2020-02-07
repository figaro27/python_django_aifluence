"""aifluence URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth.views import LoginView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView, LogoutView
from users.views import register, influencer_profile, custom_login
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='layouts/landing.html'), name='home'),
    path('login', custom_login, name='custom_login'),
    path('logout/', LogoutView.as_view(template_name='registration/login.html'), name='logout'),
    path('register/', register, name='register'),
    path('influencer/profile', influencer_profile, name='influencer_profile'),
    path('dashboard/', include('dashboard.urls')),
    path('invitations/', include('invitation.urls')),
    path('campaigns/', include('campaign.urls')),
    path('utils/', include('utils.urls')),
    path('messages/', include('message.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls', namespace='api')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
