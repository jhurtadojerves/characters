# Core imports
from django.urls import path

# Local imports
from characters.views import (
    CharacterCreate,
    CharacterList,
    CharacterUpdate,
    CharacterDetail,
)

app_name = "Character"

urlpatterns = [
    path(route="", view=CharacterList.as_view(), name="list"),
    path(route="<slug:slug>/", view=CharacterDetail.as_view(), name="detail"),
]
