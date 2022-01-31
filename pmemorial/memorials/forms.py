from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Memorial, Donation, Hospital, Profile, Fund

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class MemorialForm(forms.ModelForm):

    class Meta:
        model = Memorial
        fields = ['owner_name','owner_address_one','owner_address_two', 'owner_city', 'owner_state', 'owner_zipcode', 'pet_name', 'pet_species']

class DonationForm(forms.ModelForm):

    class Meta:
        model = Donation
        fields = '__all__'