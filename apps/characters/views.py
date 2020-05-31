# Django
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, reverse
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    TemplateView,
)

# Third party integration
from bs4 import BeautifulSoup
import requests

# Local imports
from apps.characters.models import Character
from apps.characters.forms import CharacterForm
from apps.achievements.models import Achievement, Road
from utils.is_staff import IsStaff


class CharacterList(TemplateView):
    template_name = "characters/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        characters = Character.objects.all()
        context["lideres"] = characters.filter(
            Q(range=6) | Q(is_lieutenant=True)
        ).order_by("-range")
        characters = characters.exclude(is_lieutenant=True)
        context["inities"] = characters.filter(range=1)
        context["legionarios"] = characters.filter(range=2)
        context["templarios"] = characters.filter(range=3)
        context["knights"] = characters.filter(range=4)
        context["demonhunters"] = characters.filter(range=5)
        return context


class CharacterDetail(DetailView):
    model = Character
    template_name = "characters/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        roads = Road.objects.all()
        order_achievements = dict()
        for road in roads:
            order_achievements[road.name] = Achievement.objects.filter(
                road=road
            ).order_by("points")
        context.update({"achievements": order_achievements})
        return context


class CharacterCreate(IsStaff, CreateView):
    model = Character
    form_class = CharacterForm
    template_name = "characters/form.html"

    def form_valid(self, form):
        instance = form.save()
        return redirect("Character:detail", slug=instance.slug)


class CharacterUpdate(IsStaff, UpdateView):
    model = Character
    form_class = CharacterForm
    template_name = "characters/update.html"

    def form_valid(self, form):
        character = form.save()
        return redirect(reverse("Character:detail", args=(character.slug,)))


class GetProfileInformation(TemplateView):
    """Get profile information"""

    def get(self, request, *args, **kwargs):
        url = f"http://www.harrylatino.org/user/{request.GET.get('id')}/"
        response = requests.get(url, allow_redirects=True)
        data = dict()

        if response.status_code == 200:
            html = BeautifulSoup(response.text)
            spans = html.find_all("span", {"class": "row_data"})
            messages = spans[1]
            galleons = spans[10]
            books = spans[15]
            graduate = spans[20]
            objects = spans[22]
            creatures = spans[23]
            knowledge = spans[28]
            skills = spans[29]
            medals = spans[30]

            data.update(
                {
                    "messages": f"{messages.text}".replace(".", ""),
                    "galleons": galleons.text.strip(),
                    "books": books.text.strip(),
                    "graduate": graduate.text.strip(),
                    "objects": objects.text.strip(),
                    "creatures": creatures.text.strip(),
                    "knowledge": len(f"{knowledge.text}".strip().split("\r\n")),
                    "medals": medals.text.strip(),
                    "skills": len(f"{skills.text}".strip().split("\r\n")),
                }
            )

        return JsonResponse(data)
