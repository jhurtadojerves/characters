"""Award app views"""

# Django
from django import forms
from django.contrib import messages
from django.contrib.auth import login
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import FormMixin
from django.shortcuts import redirect, reverse

# Local
from apps.characters.models import Character
from .models import Award, Category, Voting, AccessToken
from .forms import VotingForm


class AwardListView(ListView):
    """Award list view"""

    model = Award
    context_object_name = "awards"


class AwardDetailView(DetailView):
    """Award detail view"""

    model = Award
    context_object_name = "award"


class CategoryDetailView(FormMixin, DetailView):
    """Category Detail View"""

    model = Category
    context_object_name = "category"
    form_class = VotingForm

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        try:
            voting = Voting.objects.filter(user=self.request.user, category=self.object)
            if voting.exists():
                context.update(
                    {"voting": True, "options": voting.get().selected_options.all()}
                )
        except Exception as error:
            pass
        return context

    def get_form_kwargs(self):
        """Change kwargs"""
        form_kwargs = super().get_form_kwargs()
        form_kwargs.update({"category": self.get_object(), "user": self.request.user})
        return form_kwargs

    def post(self, request, *args, **kwargs):
        form_kwargs = self.get_form_kwargs()
        context = self.get_context_data(**kwargs)
        form = self.get_form()
        self.object = self.get_object()
        voting = context.get("voting", None)
        selected_options = request.POST.get("selected_options", False)
        if not self.object.award.opened:
            messages.error(request, f"{self.object.award.opened} está cerrado.")
            raise forms.ValidationError(f"{self.object.award.opened} está cerrado.")
        if len(selected_options) > self.object.max_options:
            messages.error(
                request, f"Debes elegir un máximo de {self.object.max_options}"
            )
            raise forms.ValidationError(
                f"Debes elegir un máximo de {self.object.max_options}"
            )
        if not voting:
            if form.is_valid():
                characters = Character.objects.filter(pk__in=selected_options)
                voting = form.save(commit=False)
                voting.user = request.user
                voting.category = self.object
                voting.save()
                for character in characters:
                    voting.selected_options.add(character)
                messages.success(request, "Tu voto se registró correctamente")
            else:
                messages.error(request, "Por favor corrige los errores")
                return super().form_invalid(form)
        else:
            messages.error(request, "Ya votaste antes en esta categoría")
        return redirect(
            reverse("Award:category-detail", args=(kwargs["award"], kwargs["slug"]))
        )


class LoginWithToken(DeleteView):
    """Rewrite Detail View to Login with token"""

    model = AccessToken
    slug_field = "token"
    template_name = "base.html"

    def get(self, request, *args, **kwargs):
        """Validate user and login or redirect"""
        self.object = AccessToken.objects.get(token=kwargs["uuid"])
        login(request, self.object.user)
        messages.success(request, "Te autenticaste correctamente")
        return redirect(reverse("Character:list"))
