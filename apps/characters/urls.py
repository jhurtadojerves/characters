# Core imports
from django.urls import path

# Local imports
from apps.characters.views import (
    CharacterList,
    CharacterDetail,
)

app_name = "Character"

urlpatterns = [
    path(route="", view=CharacterList.as_view(), name="list"),
    path(route="<slug:slug>/", view=CharacterDetail.as_view(), name="detail"),
]
