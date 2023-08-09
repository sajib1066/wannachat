import logging
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.models import Site

from customauth.models import User
from customauth.forms import LoginForm, SignUpForm
from customauth.sent_mail import send_mail_to_user
from django.contrib import messages
from django.db.models import Q

logger = logging.getLogger(__name__)


class UserRegistrationView(LoginView):
    """ Custom login view """
    template_name = 'customauth/signup.html'
    form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        message = ""
        if form.is_valid():
            name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            gender = request.POST.get('gender')
            country = form.cleaned_data['country']
            state = form.cleaned_data['state']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if gender:
                if password == confirm_password:
                    try:
                        user = User.objects.create_user(
                            email=email,
                            username=username,
                            password=password
                        )
                        user.profile.name = name
                        user.profile.gender = gender
                        user.profile.country = country
                        user.profile.state = state
                        user.profile.save()
                        site = Site.objects.get_current()
                        try:
                            send_mail_to_user(
                                "Welcome to Wannachat",
                                user.email,
                                'message.html',
                                {
                                    'site': site,
                                    'user': user
                                }
                            )
                        except Exception as e:
                            message = e
                        return redirect('customauth:user_login')
                    except Exception as e:
                        message = e
                else:
                    message = 'Password and confirm password must be same.'
            else:
                message = 'Please select gender.'
        else:
            print(form.errors)
            logger.error(f'Invalid form data: {form.errors}')
            message = f"{form.errors}"
        context = {
            'form': form,
            'message': message
        }
        return render(request, self.template_name, context)


class UserLoginView(LoginView):
    """ Custom login view """
    template_name = 'customauth/login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        form = self.form_class
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        form = self.form_class(request.POST)
        message = ""
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']
            try:
                get_user = User.objects.get(
                    Q(username=username_or_email) | Q(email=username_or_email)
                )
                user = authenticate(email=get_user.email, password=password)
                if user:
                    if user.verified_email:
                        login(request, user)
                        return redirect('home')
                    else:
                        messages.error(
                            request,
                            'Please verify your account. Verification link sent to your email.'  # noqa
                        )
                else:
                    messages.error(request, 'Invalid email or password')
            except User.DoesNotExist:
                messages.error(request, 'Invalid email or password')
        else:
            print(form.errors)
            logger.error(f'Invalid form data: {form.errors}')
            messages.error(
                request, "Invalid email or password. Please enter correctly."
            )
        context = {
            'form': form,
            'message': message
        }
        return render(request, self.template_name, context)


class UserLogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('customauth:user_login')
