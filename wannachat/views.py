from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q

from chatroom.models import Category, Country, Contact
from chatroom.forms import ContactForm
from customauth.models import Profile


class HomeView(View):
    """ Home view """
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        print(request, 'dada')
        try:
            country_name = request.session['country']
            print(country_name, '-------------------------------')
            country = Country.objects.get(name=country_name)
        except Exception as e:
            print(e)
            country = None
        if country:
            category_list = Category.objects.filter(
                Q(Q(country=country) & Q(is_active=True)) | Q(country__slug='world')
            ).order_by('ordering')
        else:
            try:
                country = Country.objects.get(pk=1)
                category_list = Category.objects.filter(
                    Q(Q(country=country) & Q(is_active=True)) | Q(country__slug='world')
                ).order_by('ordering')
            except Country.DoesNotExist:
                country = None
                category_list = None
        print(category_list)
        context = {
            'category_list': category_list,
            'selected_country': country,
        }
        return render(request, self.template_name, context)


class ChangeCountryView(View):

    def get(self, request, *args, **kwargs):
        country = request.GET.get('country')
        request.session['country'] = country
        print(country, '------------------------------------------')
        try:
            country_name = request.session['country']
            print(country_name, '-------------------------------')
            country = Country.objects.get(name=country_name)
        except Exception as e:
            print(e)
            country = None
        if country:
            category_list = Category.objects.filter(
                Q(Q(country=country) & Q(is_active=True)) | Q(country__slug='world')
            ).order_by('ordering')
        else:
            try:
                country = Country.objects.get(pk=1)
                category_list = Category.objects.filter(
                    Q(Q(country=country) & Q(is_active=True)) | Q(country__slug='world')
                ).order_by('ordering')
            except Country.DoesNotExist:
                country = None
                category_list = None
        context = {
            'category_list': category_list,
            'selected_country': country,
        }
        return render(request, 'home/rooms.html', context)


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


class FindFriendView(LoginRequiredMixin, View):
    template_name = 'home/find-friend.html'
    login_url = "/auth/login/"

    def get(self, request, *args, **kwargs):
        country = Country.objects.all()
        context = {
            'country_list': country,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        country = request.POST.get('country')
        state = request.POST.get('state')
        gender = request.POST.get('gender')
        print(name, country, state, gender)
        # friends = Profile.objects.filter(
        #     Q(user__username__icontains=name) | Q(name__icontains=name) | Q(
        #         gender=gender
        #     ) | Q(country__pk=country) | Q(state__pk=state)
        # )
        friends = Profile.objects.all()
        if name:
            friends = friends.filter(
                Q(user__username__icontains=name) | Q(name__icontains=name)
            )
        if gender:
            friends = friends.filter(gender=gender)
        if country:
            friends = friends.filter(country__pk=country)
        if state:
            friends = friends.filter(state__pk=state)
        friends = friends.exclude(user__email=request.user.email)
        friends = friends.exclude(user__is_superuser=True)
        print(friends)
        country_list = Country.objects.all()
        context = {
            'country_list': country_list,
            'friends': friends,
        }
        return render(request, self.template_name, context)
