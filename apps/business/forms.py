# Core imports
from django import forms

# Third party
from ckeditor.widgets import CKEditorWidget

# Local imports
from .models import Business


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('slug',)
        widgets = {
            'description': CKEditorWidget(),
        }

