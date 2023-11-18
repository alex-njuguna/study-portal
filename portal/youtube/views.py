from django.shortcuts import render
from youtubesearchpython import VideosSearch

from .forms import SearchYoutubeForm


def home(request):
    """
    display a search form
    display all videos searched
    """
    form = SearchYoutubeForm()

    return render(request, "youtube/home.html", {
        "title": "youtube",
        "form": form
    })
