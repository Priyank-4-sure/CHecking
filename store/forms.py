from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("phone", "full_name", "password1", "password2")  # Include passwords explicitly
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'input-style'}),
            'full_name': forms.TextInput(attrs={'class': 'input-style'}),
        }

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'input-style'}),
    )

    password2 = forms.CharField(
        label="Confirm Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'input-style'}),
    )
