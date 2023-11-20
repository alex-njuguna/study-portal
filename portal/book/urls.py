from django.urls import path

from . import views


app_name = "book"

urlpatterns = [
    path("", views.home, name="home"),
]