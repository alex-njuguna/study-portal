from django.urls import path

from . import views


app_name = "activity"

urlpatterns = [
    path("", views.home, name="home"),
    path("update_activity/<int:id>/", views.update_activity, name="update_activity"),
    path("delete_activity/<int:id>/", views.delete_activity, name="delete_activity"),
]
