# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import render
from django.views.generic import View


class LogoutView(LoginRequiredMixin, View):
    """
     Logs user out of the dashboard.
    """
    template_name = 'account/logout.html'

    def get(self, request):
        logout(request)
        return render(request, self.template_name)
