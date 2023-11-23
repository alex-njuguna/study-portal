import wikipedia
from django.shortcuts import render

from .forms import WikiSearchForm


def home(request):
    """
    collect search parameters
    display article from wiki
    """
    if request.method == "POST":
        form = WikiSearchForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data.get("text")

            article = wikipedia.search(text)

            context = {
                "title": "wikipedia",
                "form": form,
                "title": article.title,
                "url": article.url,
                "summary": article.summary
            }
    else:
        form = WikiSearchForm()
        context = {
            "title": "wikipedia",
            "form": form
        }

    return render(request, "wiki/home.html", context)