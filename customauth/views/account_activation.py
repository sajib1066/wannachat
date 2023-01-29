import logging
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages

from customauth.models import User

logger = logging.getLogger(__name__)


class AccountActivationView(LoginView):
    """ Custom login view """

    def get(self, request, token, *args, **kwargs):
        user = get_object_or_404(User, email_token=token)
        if user:
            user.is_active = True
            user.verified_email = True
            user.save()
            login(request, user)
        return redirect('home')
