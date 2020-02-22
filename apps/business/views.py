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


class BusinessCreateView(LoginRequiredMixin, CreateView):
    model = Business
    form_class = BusinessForm
    template_name = 'business/create.html'

    def form_valid(self, form):
        form.save()
        return redirect("Business:list")

    def handle_no_permission(self):
        return super(BusinessCreateView, self).handle_no_permission()
        messages.error(

            self.request, "Only member of staff can create characters")


class BusinessListView(ListView):
    model = Business
    template_name = 'business/list.html'
    context_object_name = "business"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['business'] = Business.objects.all().order_by('name')
        return context


class BusinessDetailView(DetailView):
    model = Business
    template_name = 'business/detail.html'


class BusinessUpdateView(LoginRequiredMixin, UpdateView):
    model = Business
    form_class = BusinessForm
    template_name = 'business/create.html'

    def form_valid(self, form):
        business = form.save(commit=False)
        business.save()
        return redirect("Business:detail", business.slug)

    def handle_no_permission(self):
        return super(BusinessCreateView, self).handle_no_permission()
        messages.error(

                self.request, "Only member of staff can update characters")