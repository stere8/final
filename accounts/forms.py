# accounts/forms.py
from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['requested_reset_password', 'allowed_password_request']