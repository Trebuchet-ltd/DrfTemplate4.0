#### forms.py
from django import forms


class SendForm(forms.Form):
    email = forms.EmailField()
    html = forms.URLField()
    subject = forms.Field()
    body = forms.Field()
    attach = forms.FileField(required=False)
