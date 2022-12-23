from django.urls import path

from chatroom import views

app_name = 'chatroom'


urlpatterns = [
    path('<int:pk>/', views.ChatRoomView.as_view(), name='room'),
    path('sidebar/', views.ChatRoomSidebarView.as_view(), name='sidebar'),
    path('<int:pk>/chatbox/', views.ChatBoxView.as_view(), name='chatbox'),
    path('<int:pk>/users/', views.ChatUsersView.as_view(), name='users'),
]
