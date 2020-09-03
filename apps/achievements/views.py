# Core imports
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class AchievementIndex(TemplateView):
    """Achievement Index"""

    template_name = "achievements/list.html"


class AchievementDetail(TemplateView):
    """Achievement Year Detail"""

    template_name = "achievements/year_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({"year": kwargs.get("year", 2020)})
        return context


class AchievementYearDetail(TemplateView):

    template_name = "achievements/month_detail.html"
