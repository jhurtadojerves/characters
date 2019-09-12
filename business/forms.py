# Core imports
from django import forms

# Local imports
from .models import Business


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('slug',)
