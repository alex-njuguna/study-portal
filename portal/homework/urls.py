from django.urls import path

from . import views


app_name = "homework"

urlpatterns = [
    path("", views.home, name="home"),
    path("update-homework/<int:id>/", views.update_homework, name="update_homework"),

]

