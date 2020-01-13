from django import forms

from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.views import PasswordResetView
from django.forms import TextInput, EmailInput
from django.forms.widgets import Input

from users.models import User, Influencer

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    username = forms.CharField(label='User Name')
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
    
    def clean_username(self):
        to_check = self.cleaned_data.get('username')
        if to_check and (User.objects.filter(username=to_check).exists()):
            raise forms.ValidationError('Username already exists', code='username_exist')
        return to_check

    def clean_email(self):
        to_check = self.cleaned_data.get('email')
        if to_check and (User.objects.filter(email=to_check).exists()):
            raise forms.ValidationError('Email already exists', code='email_exist')
        return to_check

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match', code='password_mismatch')
        return password2

class InfluencerProfileForm(forms.ModelForm):
    class Meta:
        model = Influencer
        fields = ['instagram_account', 'facebook_account', 'twitter_account']