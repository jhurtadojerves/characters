from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DetailView,
    TemplateView
)

# Local imports
from .models import Business
from .forms import BusinessForm


class BusinessListView(ListView):
    model = Business
    template_name = 'business/list.html'
    context_object_name = "business"


class BusinessCreate(LoginRequiredMixin, CreateView):
    model = Business
    form_class = BusinessForm
    template_name = 'business/create.html'

    def form_valid(self, form):
        form.save()
        return redirect("Business:list")

    def handle_no_permission(self):
        messages.error(
            self.request, "Only member of staff can create characters")
        return super(BusinessCreate, self).handle_no_permission()
