# Core imports
from django.urls import path

# Local imports
from .views import (
    BusinessListView,
    BusinessCreateView,
    BusinessDetailView,
    BusinessUpdateView,
)

app_name = "Business"


urlpatterns = [
    path(route="", view=BusinessListView.as_view(), name="list"),
    path(route="create/", view=BusinessCreateView.as_view(), name="create"),
    path(route="<slug:slug>/", view=BusinessDetailView.as_view(), name="detail"),
    path(route="<slug:slug>/editar", view=BusinessUpdateView.as_view(), name="update"),

]
