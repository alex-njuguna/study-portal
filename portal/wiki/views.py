import wikipedia
from django.shortcuts import render

from .forms import WikiSearchForm


def home(request):
    """
    collect search parameters
    display article from wikipedia
    """
    if request.method == "POST":
        form = WikiSearchForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data.get("text")

            articles = wikipedia.search(text)

            if articles:

                article_title = articles[0]

                article = wikipedia.page(article_title)

                context = {
                    "title": "wikipedia",
                    "form": form,
                    "heading": article.title,
                    "url": article.url,
                    "summary": article.summary
                }
            else:
                context = {
                "title": "wikipedia",
                "form": form,
                "error_message": "No results found."
            }
    else:
        form = WikiSearchForm()
        context = {
            "title": "wikipedia",
            "form": form
        }

    return render(request, "wiki/home.html", context)