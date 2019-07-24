# Django imports.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View


class Index(LoginRequiredMixin, View):
    """
    Display homepage of the dashboard.
    """
    context = {}
    template_name = 'dashboard/author/index.html'

    def get(self, request, *args, **kwargs):
        """
        Returns the author details
        """
        return render(request, self.template_name, self.context)
