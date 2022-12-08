from django.views.generic import View
from django.shortcuts import render


class HomeView(View):
    """ Home view """
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)
