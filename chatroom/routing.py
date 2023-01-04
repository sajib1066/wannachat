from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/<int:roomid>/', consumers.ChatConsumer.as_asgi()),
]
