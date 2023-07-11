from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.contrib.auth.decorators import login_required
from .views import home, profile


urlpatterns = [
    path("", login_required(home.as_view()), name="home"),
    path("signup/", views.signup, name="signup"),
    path(
        "login/",
        auth_view.LoginView.as_view(template_name="user/login.html"),
        name="login",
    ),
    path("profile", login_required(profile.as_view()), name="profile"),
]
