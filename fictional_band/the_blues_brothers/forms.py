from django import forms
from .models import Member


class ContactForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'message']
