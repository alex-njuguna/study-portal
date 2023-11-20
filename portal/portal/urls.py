from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include("dashboard.urls")),
    path("note/", include("note.urls")),
    path("homework/", include("homework.urls")),
    path("youtube/", include("youtube.urls")),
    path("activity/", include("activity.urls")),
    path("book/", include("book.urls")),


]
