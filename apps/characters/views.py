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
from django.http import Http404

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
        characters = Character.objects.exclude(active=False)
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

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object.active and not request.user.is_staff:
            raise Http404("El personaje no existe")
        return super(CharacterDetail, self).get(request)


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
        url = f"http://www.harrylatino.org/user/{request.GET.get('id')}-xxx/"
        response = requests.get(url, allow_redirects=True)
        output = dict({"message": "Se produjo un error :c"})

        if response.status_code == 301:
            url = ((response.headers["Refresh"]).split(";")[1]).replace("url=", "")
            response = requests.get(url, allow_redirects=True)

        if response.status_code == 200:
            html = BeautifulSoup(response.text)
            data = html.select("ul.cProfileFields > li.ipsType_break > div.ipsDataItem_generic > div.ipsContained")
            labels = html.select("ul.cProfileFields > li.ipsType_break > span.ipsType_break")
            nick_name = str(html.select('title')[0].text).split("-")[0].strip()
            messages_data = html.select("#elProfileStats > ul.ipsPos_left > li")
            messages = (messages_data[0].text.replace("Mensajes", "").strip().replace(".", ""))
            graduate = ""
            current_level = 0
            galleons = 0
            book = ""
            points_objects = 0
            points_creatures = 0
            knowledge = ""
            skills = ""
            badges = 0
            team = ""
            dungeons = 0
            fabrication = 0

            for i in range(len(data)):
                if labels[i].text.strip() == "Nivel Mágico":
                    current_level = int(data[i].text.strip())
                if labels[i].text.strip() == "Graduación":
                    graduate = data[i].text.strip()
                if labels[i].text.strip() == "Galeones":
                    galleons = int(data[i].text.strip())
                if labels[i].text.strip() == "Libros de Hechizos":
                    book = data[i].text.strip()
                if labels[i].text.strip() == "Puntos de Poder en Objetos":
                    points_objects = int(data[i].text.strip())
                if labels[i].text.strip() == "Puntos de Poder en Criaturas":
                    points_creatures = int(data[i].text.strip())
                if labels[i].text.strip() == "Conocimientos":
                    knowledge = data[i].text.strip()
                if labels[i].text.strip() == "Habilidades Mágicas":
                    skills = data[i].text.strip()
                if labels[i].text.strip() == "Medallas":
                    badges = int(data[i].text.strip())
                if labels[i].text.strip() == "Bando":
                    team = data[i].text.strip()
                if labels[i].text.strip() == "Puntos en Mazmorras":
                    dungeons = data[i].text.strip()
                if labels[i].text.strip() == "Puntos de Fabricación":
                    fabrication = data[i].text.strip()

            number_of_knowledge = 0 if knowledge == "" else len(knowledge.split("\n"))
            number_of_skills = 0 if skills == "" else len(skills.split("\n"))
            output.update(
                {
                    "messages": messages,
                    "galleons": galleons,
                    "books": book,
                    "graduate": graduate,
                    "objects": points_objects,
                    "creatures": points_creatures,
                    "knowledge": number_of_knowledge,
                    "medals": badges,
                    "skills": number_of_skills,
                    "team": team,
                    "dungeons": dungeons,
                    "fabrication": fabrication,
                    "current_level": current_level,
                    "nick": nick_name,
                    "message": "Datos obtenidos correctamente:D"
                }
            )

        return JsonResponse(output, status=response.status_code)
