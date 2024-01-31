from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views
from django.contrib.auth.decorators import login_required
from .decorators import admin_required

urlpatterns = [
    path("", home.as_view(), name="home"),
    # user authentications
    path("signup/", views.signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.profile, name="profile"),
]
