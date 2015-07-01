from django import forms
from django.core.exceptions import ValidationError

from contacts.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact

   
