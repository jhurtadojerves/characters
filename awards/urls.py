"""Urls to awards module"""

# Django imports
from django.urls import path

app_name = "Award"


from .views import AwardListView, AwardDetailView

urlpatterns = [
    path(route="", view=AwardListView.as_view(), name="list"),
    path(route="<slug:slug>", view=AwardDetailView.as_view(), name="detail"),
]
