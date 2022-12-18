from django.urls import path

from customauth import views

app_name = 'customauth'


urlpatterns = [
    path('admin-login/', views.AdminLoginView.as_view(), name='admin_login'),
    path('admin-logout/', views.user_logout, name='logout'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('signup/', views.UserRegistrationView.as_view(), name='user_signup'),
]
