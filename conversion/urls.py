from django.urls import path

from . import views


app_name = "conversion"

urlpatterns = [
    path("", views.index, name="index"),
]