from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput, EmailInput

class CustomAuthForm(AuthenticationForm):
    email = forms.CharField(widget=TextInput(attrs={'class':'form-control', 'required':'required'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class':'form-control ','placeholder':'Password', 'required':'required'}))

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','required':'required'}))
    

    class Meta:
        model = CustomUser
        fields = {'email',} 
        widgets = {
        'email': EmailInput(attrs={'class':'form-control', 'placeholder':'Email', 'required':'required'}),
        }
