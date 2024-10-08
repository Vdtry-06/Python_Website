from django import forms
from django.contrib.auth.models import User
from App.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField (widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ("username", 'email', 'password')
        help_texts = {
            'username': None,  # Bỏ help_text để không hiển thị thông báo
        }

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)
    