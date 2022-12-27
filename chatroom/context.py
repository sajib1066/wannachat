from chatroom.models import Country


def get_country_list(request):
    country_list = Country.objects.all()
    context = {
        'country_list': country_list
    }
    return context
