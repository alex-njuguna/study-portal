from django.urls import path

from . import views


app_name = "dashboard"

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_user, name="login"),
    path("profile/", views.profile, name="profile"),
    path("signout/", views.signout, name="signout")
]

