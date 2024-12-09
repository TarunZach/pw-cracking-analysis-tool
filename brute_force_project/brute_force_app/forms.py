# brute_force_app/forms.py

from django import forms

class PasswordForm(forms.Form):
    password = forms.CharField(label='Enter Password', max_length=255)
