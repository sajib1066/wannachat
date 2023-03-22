from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from customauth.models import User
from chatroom.models import DirectmessageUser


class AddFriendView(LoginRequiredMixin, View):

    def get(self, request, userid, *args, **kwargs):
        user = User.objects.get(pk=userid)
        friend = DirectmessageUser.objects.get_or_create(
            me=request.user,
            friends=user
        )
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class MakeFriendView(LoginRequiredMixin, View):

    def get(self, request, userid, *args, **kwargs):
        user = User.objects.get(pk=userid)
        friend = DirectmessageUser.objects.get(
            me=request.user,
            friends=user
        )
        friend.friend_type = 'buddies'
        friend.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class MakeFamilyMemberView(LoginRequiredMixin, View):

    def get(self, request, userid, *args, **kwargs):
        user = User.objects.get(pk=userid)
        friend = DirectmessageUser.objects.get(
            me=request.user,
            friends=user
        )
        friend.friend_type = 'family'
        friend.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class MakeCoWorkerView(LoginRequiredMixin, View):

    def get(self, request, userid, *args, **kwargs):
        user = User.objects.get(pk=userid)
        friend = DirectmessageUser.objects.get(
            me=request.user,
            friends=user
        )
        friend.friend_type = 'co-workers'
        friend.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
