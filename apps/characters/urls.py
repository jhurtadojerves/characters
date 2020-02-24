# Core imports
from django.urls import path

# Local imports
from apps.characters.views import (
    CharacterCreate,
    CharacterDetail,
    CharacterList,
    CharacterUpdate,
)

app_name = "Character"

urlpatterns = [
    path(route="", view=CharacterList.as_view(), name="list"),
    path(route="create/", view=CharacterCreate.as_view(), name="create"),
    path(route="<slug:slug>/", view=CharacterDetail.as_view(), name="detail"),
    path(route="<slug:slug>/update/", view=CharacterUpdate.as_view(), name="update"),
]
