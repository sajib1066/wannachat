from django.db.models import Q
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from chatroom.models import SubCategory, ChatRoomUser, RoomMessage, DirectMessage, DirectmessageUser
from customauth.models import User


class ChatDashboardView(LoginRequiredMixin, View):
    template_name = "chatroom/dash.html"
    model = SubCategory
    login_url = "/auth/login/"

    def get(self, request, *args, **kwargs):
        chatrooms = ChatRoomUser.objects.filter(user=request.user)
        direct_messages = DirectmessageUser.objects.filter(me=request.user)
        context = {
            'user': request.user,
            'direct_messages': direct_messages,
            'chatrooms': chatrooms,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(self.model, pk=kwargs.get('pk'))
        message_list = RoomMessage.objects.filter(room=obj)
        photo = request.FILES.get('photo')
        name = request.POST.get('name')
        bio = request.POST.get('bio')
        address = request.POST.get('address')
        user = request.user
        if name:
            user.profile.name = name
        if bio:
            user.profile.bio = bio
        if address:
            user.profile.address = address
        if photo:
            user.profile.avatar = photo
        user.profile.save()
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
        chatrooms = ChatRoomUser.objects.filter(user=request.user)
        context = {
            'user': request.user,
            'obj': obj,
            'chatrooms': chatrooms,
            'messages': message_list,
        }
        return render(request, self.template_name, context)
