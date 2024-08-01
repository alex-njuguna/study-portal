from django.urls import path

from . import views


app_name = "note"

urlpatterns = [
    path("", views.home, name="home"),
    path("note-detail/<int:id>/", views.note_detail, name="note_detail"),
    path("note-delete/<int:id>/", views.note_delete, name="note_delete"),
]