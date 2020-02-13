"""Forms class file"""

from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Voting, Category


class VotingForm(ModelForm):
    class Meta:
        model = Voting
        fields = ("selected_options",)

    def __init__(self, *args, **kwargs):
        """Define initial values"""
        self.category = kwargs.pop("category", None)
        super().__init__(*args, **kwargs)
        self.fields["selected_options"].queryset = self.category.participants.all()
