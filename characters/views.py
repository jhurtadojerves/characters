# Core imports
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DetailView,
    TemplateView
)

# Local imports
from characters.models import Character
from characters.forms import CharacterForm


class CharacterList(TemplateView):
    template_name = 'characters/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        characters = Character.objects.all()
        context["inities"] = characters.filter(range=1)
        context["legionarios"] = characters.filter(range=2)
        context["templarios"] = characters.filter(range=3)
        context["knights"] = characters.filter(range=4)
        context["demonhunters"] = characters.filter(range=5)
        context["lideres"] = characters.filter(range=6)
        return context


class CharacterDetail(DetailView):
    model = Character
    template_name = 'characters/detail.html'


class CharacterCreate(LoginRequiredMixin, CreateView):
    model = Character
    form_class = CharacterForm
    template_name = 'characters/create.html'

    def form_valid(self, form):
        form.save()
        return redirect("Character:list")

    def handle_no_permission(self):
        messages.error(
            self.request, "Only member of staff can create characters")
        return super(CharacterCreate, self).handle_no_permission()


class CharacterUpdate(LoginRequiredMixin, UpdateView):
    model = Character
    form_class = CharacterForm
    template_name = 'characters/update.html'
    success_url = '../'
