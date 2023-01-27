from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse

from chatroom.models import Category, Country


class HomeView(View):
    """ Home view """
    template_name = 'home.html'

    def get(self, request):
        try:
            country_name = request.session['country']
            print(country_name, '-------------------------------')
            country = Country.objects.get(name=country_name)
        except Exception as e:
            print(e)
            country = None
        if country:
            category_list = Category.objects.filter(country=country).order_by('ordering')
        else:
            category_list = Category.objects.all().order_by('ordering')
            country = Country.objects.get(pk=1)
        context = {
            'category_list': category_list,
            'selected_country': country,
        }
        return render(request, self.template_name, context)


class ChangeCountryView(View):

    def get(self, request, *args, **kwargs):
        country = request.GET.get('country')
        request.session['country'] = country
        return HttpResponse('Done')
