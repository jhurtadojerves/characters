# Core imports
from django.urls import path

app_name = "Achievement"

# Local imports
from .views import AchievementIndex, AchievementDetail


urlpatterns = [
    path(route="", view=AchievementIndex.as_view(), name="list"),
    path(route="<int:year>/", view=AchievementDetail.as_view(), name="year_list"),
    path(
        route="<int:year>/<slug:month>/",
        view=AchievementDetail.as_view(),
        name="year_detail",
    ),
]
