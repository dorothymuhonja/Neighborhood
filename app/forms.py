from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=250, help_text='Required. Please enter a valid email address')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=250)

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']


class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['admin']


class BusinessForm(forms.ModelForm):
    class Meta:
     model = Business
     exclude = ['user', 'neighborhood']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'neighborhood']
