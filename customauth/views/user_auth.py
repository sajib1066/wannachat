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
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password == confirm_password:
                try:
                    user = User.objects.create_user(
                        email=email,
                        password=password
                    )
                    user.profile.name = name
                    user.profile.save()
                    site = Site.objects.get_current()
                    print(site, '************')
                    send_mail_to_user(
                        "Welcome to Wannachat",
                        user.email,
                        'message.html',
                        {
                            'site': site,
                            'user': user
                        }
                    )
                    return redirect('customauth:user_login')
                except Exception as e:
                    message = e
            else:
                message = 'Password and confirm password must be same.'
        else:
            print(form.errors)
            logger.error(f'Invalid form data: {form.errors}')
            message = "Invalid email or password. Please enter correctly."
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
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                if user.verified_email:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'Please verify your account. Verification link sent to your email.')
            else:
                messages.error(request, 'Invalid email or password')
        else:
            print(form.errors)
            logger.error(f'Invalid form data: {form.errors}')
            messages.error(request, "Invalid email or password. Please enter correctly.")
        context = {
            'form': form,
            'message': message
        }
        return render(request, self.template_name, context)


class UserLogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('customauth:user_login')
