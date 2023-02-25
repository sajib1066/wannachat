# DJANGO IMPORTS
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# PYTHON IMPORTS
import logging


logger = logging.getLogger(__name__)


def send_mail_to_user(
    subject, mail_receiver, template, context=None, request=None
):
    """
    Sends a HTML email to the receiver.
    Returns a boolean status flag of True once count is more than 0.
    """
    # get site info
    if request:
        current_site = get_current_site(request)
    else:
        current_site = Site.objects.get_current()

    # site context
    context_site = {
        'site_name': current_site.name,
        'domain': current_site.domain,
        'protocol': 'https'
    }

    # update context
    if context:
        context.update(context_site)
    else:
        context = context_site

    # html render
    html_message = render_to_string(template, context)
    plain_message = strip_tags(html_message)

    receiver = []
    if isinstance(mail_receiver, str):
        receiver = [mail_receiver, ]

    # send email
    send_mail(
        subject, plain_message, settings.DEFAULT_FROM_EMAIL, receiver,
        html_message=html_message
    )
