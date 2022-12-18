from django.urls import path

from chatroom import views

app_name = 'chatroom'


urlpatterns = [
    path('<int:pk>/', views.ChatRoomView.as_view(), name='room')
]
