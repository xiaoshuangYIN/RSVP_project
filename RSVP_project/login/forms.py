from django.contrib.auth.models import User as User_Model
from django import forms

'''
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    # the info about the class
    class Meta:
        model = User_Model
        fields = ('username', 'email', 'password')
'''
'''
class UserLoginForm(forms.Form):
    User_name = forms.CharField(label = 'User name', max_length=100)
    Password = forms.CharField(label = 'Password', max_length=100)
'''
class UserForm(forms.Form):
    User_name = forms.CharField(label = 'User name', max_length=100)
    Email = forms.CharField(label = 'Email', max_length=100)
    Password = forms.CharField(label = 'Password', max_length=100)
