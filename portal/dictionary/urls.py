from django.urls import path

from . import views


app_name = "dictionary"

urlpatterns = [
    path("", views.home, name="home")
]