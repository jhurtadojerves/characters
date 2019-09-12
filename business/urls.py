# Core imports
from django.urls import path

# Local imports
from .views import (
    BusinessListView,
    BusinessCreate
)

app_name = "Business"


urlpatterns = [
    path(route="", view=BusinessListView.as_view(), name="list"),
    path(route="create/", view=BusinessCreate.as_view(), name="create"),

]
