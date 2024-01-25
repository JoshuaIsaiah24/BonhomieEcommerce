from django import forms
from django.core.validators import EmailValidator


class contactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    message = forms.CharField(widget=forms.Textarea)