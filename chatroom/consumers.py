import json

from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from chatroom.models import SubCategory, RoomMessage, DirectMessage

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['roomid']
        self.room_group_name = 'chat_%s' % self.room_id

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        print(data)
        message = data['message']
        email = data['email']
        room = data['room']

        await self.save_message(email, room, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'email': email
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        email = event['email']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'email': email
        }))

    @sync_to_async
    def save_message(self, email, room, message):
        user = User.objects.get(email=email)
        room = SubCategory.objects.get(pk=room)
        RoomMessage.objects.create(room=room, user=user, message=message)
