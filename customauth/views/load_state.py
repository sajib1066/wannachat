from django.shortcuts import render

from chatroom.models import Country, State


def load_state_view(request):
    country = request.GET.get('country')
    state_list = State.objects.filter(country__pk=country)
    context = {
        'state_list': state_list,
    }
    return render(request, 'customauth/load_state.html', context)
