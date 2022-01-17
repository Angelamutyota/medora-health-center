from django import forms
from django.forms import fields
from .models import Profile, Vitals, vitals
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','bio','contact']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class VitalsForm(forms.ModelForm):
    class Meta:
        model = Vitals
        fields = ['temperature', 'pulserate', 'bloodpressure', 'symptoms']
