from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label='Login',widget=forms.TextInput(attrs={'class':'form-input'}))
    email = forms.EmailField(label='Email', widget= forms.EmailInput(attrs= {'class': 'form-input'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label='Repeat Password',widget=forms.PasswordInput(attrs={'class':'form-input'}))


    class Meta:
        model = User
        fields = ('username','email','password1','password2')




class LoginUserForm(AuthenticationForm):

     username = forms.CharField(label='Login',widget=forms.TextInput(attrs={'class':'form-input'}))
     password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-input'}))

class AddVideoForm(forms.ModelForm):

    title = forms.CharField(label = 'title',widget = forms.TextInput())
    description = forms.CharField(label ='description',widget= forms.TextInput())
    video = forms.FileField(label = 'video',widget= forms.FileInput())
    class Meta:
        model = Videos
        fields = ('title','description','video')