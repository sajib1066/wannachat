from django.urls import path

from customauth import views

app_name = 'customauth'


urlpatterns = [
    path('admin-login/', views.AdminLoginView.as_view(), name='admin_login'),
    path('logout/', views.user_logout, name='logout'),
]
