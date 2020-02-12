from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import User, Influencer

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username', 'first_name', 'last_name','is_staff', 'is_active', 'is_client', 'is_influencer']
    list_filter = ('is_staff', 'is_active', 'is_client', 'is_influencer')
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser','is_client', 'is_influencer',
                                       'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
class InfluencerAdmin(admin.ModelAdmin):
    list_display = ('user', 'instagram_account', 'facebook_account', 'twitter_account')

admin.site.register(User, CustomUserAdmin)
admin.site.register(Influencer, InfluencerAdmin)
