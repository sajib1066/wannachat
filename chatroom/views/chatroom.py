from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from chatroom.models import Category, SubCategory


class ChatRoomView(View):
    template_name = "chatroom/room.html"
    model = SubCategory
    # login_url = "/auth/login/"

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(self.model, pk=kwargs.get('pk'))
        context = {
            'obj': obj,
        }
        return render(request, self.template_name, context)
