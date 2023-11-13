from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'gender', 'year_of_birth', 'tg', 'phone', 'about_ur_self', 'photo']