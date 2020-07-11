from django import forms
from system.models import Patients


class LoginForm(forms.Form):
   user = forms.CharField(max_length=100)
   password = forms.CharField(widget=forms.PasswordInput())