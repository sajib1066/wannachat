from django.urls import path

from chatroom import views

app_name = 'chatroom'


urlpatterns = [
    path('<int:pk>/', views.ChatRoomView.as_view(), name='room'),
    path('direct/<int:pk>/', views.DirectChatView.as_view(), name='direct_chat'),
    path('sidebar/', views.ChatRoomSidebarView.as_view(), name='sidebar'),
    path('<int:pk>/chatbox/', views.ChatBoxView.as_view(), name='chatbox'),
    path('<int:pk>/users/', views.ChatUsersView.as_view(), name='users'),
    path(
        'send-room-message/', views.SendRoomMessageView.as_view(),
        name='send_room_message'
    ),
    path('ajax/custom/room/', views.ajax_custom_room, name='ajax_custom_room')
]
