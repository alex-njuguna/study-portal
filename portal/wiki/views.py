import wikipedia
from django.shortcuts import render

from .forms import WikiSearchForm


def home(request):
    """
    collect search parameters
    display article from wiki
    """
    form = WikiSearchForm()

    return render(request, "wiki/home.html", {
        "title": "wikipedia",
        "form": form
    })