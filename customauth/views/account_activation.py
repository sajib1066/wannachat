import logging
from django.views.generic import View
from django.shortcuts import redirect, get_object_or_404

from customauth.models import User

logger = logging.getLogger(__name__)


class AccountActivationView(View):
    """ Custom login view """

    def get(self, request, token, *args, **kwargs):
        user = get_object_or_404(User, email_token=token)
        if user:
            user.is_active = True
            user.verified_email = True
            user.save()
        return redirect('customauth:user_login')
