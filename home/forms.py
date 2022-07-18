#### forms.py
from django import forms


class SendForm(forms.Form):
    email = forms.EmailField()