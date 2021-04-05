from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta: #gives a nested namespace for the confighurations and keeps the configurations in one place
        model = User
        fields = ['username', 'email', 'password1', 'password2']

