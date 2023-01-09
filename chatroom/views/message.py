from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib import messages

from chatroom.models import SubCategory, ChatRoomUser, RoomMessage


class SendRoomMessageView(View):

    def get(self, request, *args, **kwargs):
        roomid = request.GET.get('roomid')
        email = request.GET.get('email')
        message = request.GET.get('message')
        room = SubCategory.objects.get(id=roomid)
        message_list = RoomMessage.objects.create(
            room=room,
            user=request.user,
            message=message,
        )
        return HttpResponse('SUCCESS')
