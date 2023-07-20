from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.RegisterAPI.as_view(), name='user-register'),
    path('login/', views.LoginAPI.as_view(), name='user-login'),
    path('logout/', views.LogoutAPI.as_view(), name='user-logout'),
    path("fetch-users/", views.UsersListAPI.as_view(), name='fetch-users'),
    path("users/<username>/", views.UsersDetailAPI.as_view(), name='user-detail'),
]
