from django.db.models import Q
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from chatroom.models import SubCategory, ChatRoomUser, RoomMessage, DirectMessage
from customauth.models import User


class ChatRoomView(LoginRequiredMixin, View):
    template_name = "chatroom/room.html"
    model = SubCategory
    login_url = "/auth/login/"

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(self.model, pk=kwargs.get('pk'))
        message_list = RoomMessage.objects.filter(room=obj)
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
        all_direct_chat = request.user.me.all()
        buddies = all_direct_chat.filter(friend_type='buddies')
        family_members = all_direct_chat.filter(friend_type='family')
        co_workers = all_direct_chat.filter(friend_type='co-workers')
        context = {
            'user': request.user,
            'chatroom': obj,
            'chatrooms': chatrooms,
            'messages': message_list,
            'all_direct_chat': all_direct_chat,
            'buddies': buddies,
            'family_members': family_members,
            'co_workers': co_workers
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
            'chatroom': obj,
            'chatrooms': chatrooms,
            'messages': message_list,
        }
        return render(request, self.template_name, context)


class DirectChatView(LoginRequiredMixin, View):
    template_name = "chatroom/direct_room.html"
    model = DirectMessage
    login_url = "/auth/login/"

    def get(self, request, chatroom, pk, *args, **kwargs):
        chatroom = get_object_or_404(SubCategory, pk=chatroom)
        obj = get_object_or_404(User, pk=pk)
        message_list = DirectMessage.objects.filter(
            Q(sender_user=obj, receiver_user=request.user) | Q(sender_user=request.user, receiver_user=obj)
        )
        context = {
            'user': request.user,
            'obj': obj,
            'chatroom': chatroom,
            'messages': message_list,
        }
        return render(request, self.template_name, context)

    def post(self, request, chatroom, pk, *args, **kwargs):
        chatroom = get_object_or_404(SubCategory, pk=chatroom)
        obj = get_object_or_404(User, pk=pk)
        photo = request.FILES.get('photo')
        name = request.POST.get('name')
        bio = request.POST.get('bio')
        address = request.POST.get('address')
        user = request.user
        print(name, bio, address, user, photo, "*" * 100)
        if name:
            user.profile.name = name
        if bio:
            user.profile.bio = bio
        if address:
            user.profile.address = address
        if photo:
            user.profile.avatar = photo
        user.profile.save()
        message_list = DirectMessage.objects.filter(
            Q(sender_user=obj, receiver_user=request.user) | Q(sender_user=request.user, receiver_user=obj)
        )
        context = {
            'user': request.user,
            'obj': obj,
            'chatroom': chatroom,
            'messages': message_list,
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
