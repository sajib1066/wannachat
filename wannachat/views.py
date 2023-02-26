from django.views.generic import View, TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from chatroom.models import Category, Country, Contact
from chatroom.forms import ContactForm


class HomeView(View):
    """ Home view """
    template_name = 'home/home.html'

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
    template_name = 'home/faq.html'


class TOSPageView(TemplateView):
    template_name = 'home/tos.html'


class ChatRulesPageView(TemplateView):
    template_name = 'home/chat_rules.html'


class SafetyTipsPageView(TemplateView):
    template_name = 'home/safety_tips.html'


class PrivacyPolicyPageView(TemplateView):
    template_name = 'home/privacy_policy.html'


class CookiePolicyPageView(TemplateView):
    template_name = 'home/cookie_policy.html'


class CookieSettingsPageView(TemplateView):
    template_name = 'home/cookie_settings.html'


class ContactPageView(View):
    template_name = 'home/contact.html'
    model = Contact
    form_class = ContactForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message submitted successfully.')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)
