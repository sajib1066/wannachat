from django.views.generic import View
from django.shortcuts import render

from chatroom.models import Category


class HomeView(View):
    """ Home view """
    template_name = 'home.html'

    def get(self, request):
        category_list = Category.objects.all()
        context = {
            'category_list': category_list
        }
        return render(request, self.template_name, context)
