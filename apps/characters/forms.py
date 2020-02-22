# Core imports
from django import forms

# Local imports
from apps.characters.models import Character


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        exclude = ("slug",)
