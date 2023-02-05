from django.views.generic import View, TemplateView
from django.shortcuts import render
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
            category_list = Category.objects.filter(
                country=country, is_active=True
            ).order_by('ordering')
        else:
            try:
                country = Country.objects.get(pk=1)
                category_list = Category.objects.filter(
                    country=country, is_active=True
                ).order_by('ordering')
            except Country.DoesNotExist:
                country = None
                category_list = None
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


class FAQPageView(TemplateView):
    template_name = 'pages/faq.html'


class TOSPageView(TemplateView):
    template_name = 'pages/tos.html'


class ChatRulesPageView(TemplateView):
    template_name = 'pages/chat_rules.html'


class SafetyTipsPageView(TemplateView):
    template_name = 'pages/safety_tips.html'


class PrivacyPolicyPageView(TemplateView):
    template_name = 'pages/privacy_policy.html'


class CookiePolicyPageView(TemplateView):
    template_name = 'pages/cookie_policy.html'


class CookieSettingsPageView(TemplateView):
    template_name = 'pages/cookie_settings.html'
