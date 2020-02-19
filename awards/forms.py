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
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        queryset = self.category.participants.all()
        if (
            hasattr(self.user, "token")
            and self.user.token
            and not self.category.self_voting
        ):
            queryset = queryset.exclude(pk=self.user.token.character.pk)
        self.fields["selected_options"].queryset = queryset
