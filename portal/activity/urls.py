from django.urls import path

from . import views


app_name = "activity"

urlpatterns = [
    path("", views.home, name="home"),
]
