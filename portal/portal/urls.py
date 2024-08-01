from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include("dashboard.urls")),
    path("note/", include("note.urls")),
    path("homework/", include("homework.urls")),
    path("youtube/", include("youtube.urls")),
    path("activity/", include("activity.urls")),
    path("book/", include("book.urls")),
    path("dictionary/", include("dictionary.urls")),
    path("wiki/", include("wiki.urls")),
    path("conversion/", include("conversion.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)