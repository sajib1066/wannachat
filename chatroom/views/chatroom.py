from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from chatroom.models import SubCategory, ChatRoomUser


class ChatRoomView(LoginRequiredMixin, View):
    template_name = "chatroom/room.html"
    model = SubCategory
    login_url = "/auth/login/"

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(self.model, pk=kwargs.get('pk'))
        try:
            ChatRoomUser.objects.get(
                user=request.user,
                room=obj
            )
        except ChatRoomUser.DoesNotExist:
            if obj.current_users < obj.max_user:
                ChatRoomUser.objects.create(
                    user=request.user,
                    room=obj
                )
            else:
                messages.warning(request, "This room is full now.")
                return redirect('home')
        context = {
            'obj': obj,
        }
        return render(request, self.template_name, context)


class ChatRoomSidebarView(LoginRequiredMixin, View):
    template_name = "chatroom/userpanel.html"
    model = SubCategory
    login_url = "/auth/login/"

    def get(self, request, *args, **kwargs):
        obj = None
        context = {
            'obj': obj,
        }
        return render(request, self.template_name, context)


class ChatBoxView(LoginRequiredMixin, View):
    template_name = "chatroom/chatbox.html"
    model = SubCategory
    login_url = "/auth/login/"

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(self.model, pk=kwargs.get('pk'))
        context = {
            'obj': obj,
        }
        return render(request, self.template_name, context)


class ChatUsersView(LoginRequiredMixin, View):
    template_name = "chatroom/chatusers.html"
    model = SubCategory
    login_url = "/auth/login/"

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(self.model, pk=kwargs.get('pk'))
        context = {
            'obj': obj,
        }
        return render(request, self.template_name, context)
