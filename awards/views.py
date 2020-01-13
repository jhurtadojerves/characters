"""Award app views"""

# Django
from django.views.generic import ListView, DetailView

# Local
from .models import Award


class AwardListView(ListView):
    """Award list view"""

    model = Award
    context_object_name = "awards"


class AwardDetailView(DetailView):
    """Award detail view"""

    model = Award
    context_object_name = "award"
