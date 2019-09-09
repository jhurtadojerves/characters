# Core imports
from django import forms

# Local imports
from characters.models import Character


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        exclude = ('slug',)
