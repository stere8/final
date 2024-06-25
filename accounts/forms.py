# accounts/forms.py
from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput()  # Set the widget to PasswordInput
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['requested_reset_password', 'allowed_password_request']