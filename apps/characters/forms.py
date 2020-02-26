# Core imports
from django import forms

# Third Party Integration
from ckeditor.widgets import CKEditorWidget


# Local imports
from apps.characters.models import Character


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        exclude = ("slug",)
        widgets = {
            "characteristics": CKEditorWidget(),
            "job_description": CKEditorWidget(),
            "patronus": CKEditorWidget(),
            "wand": CKEditorWidget(),
        }
