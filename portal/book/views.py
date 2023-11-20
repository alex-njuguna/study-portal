from django.shortcuts import render, redirect
import requests

from .forms import SearchBookForm


def home(request):
    """
    display a search form to search books
    display 10 books searched
    api - https://www.googleapis.com/books/v1/volumes?q={search terms}
    """

    form = SearchBookForm()

    return render(request, "book/home.html", {
        "title": "books",
        "form": form
    })

