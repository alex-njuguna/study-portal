from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = "book"

urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.books, name="books"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
