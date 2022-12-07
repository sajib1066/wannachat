from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


class DashboardView(LoginRequiredMixin, View):
    """ Dashboard view """
    template_name = 'dashboard/dashboard.html'
    login_url = "/auth/admin-login/"

    def get(self, request):
        return render(request, self.template_name)
