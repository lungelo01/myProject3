from django import forms
from .models import Member


class ContactForm(forms.ModelForm):
    """Class contains contact forms about details of members."""
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'message']
