# .\Lindy_Assesser\user_management\forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from user_management.models import CustomUser

class CustomAuthForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
    
    def clean_username(self):
        return self.cleaned_data['username']
        
class CustomUserCreationForm(UserCreationForm):
   
    class Meta(UserCreationForm.Meta):
        model = CustomUser 
        fields = ('email','full_name',)


class CustomUserChangeForm(UserChangeForm):
   
    class Meta:
        model = CustomUser
        fields = ('email', 'full_name', 'is_staff', 'is_active')