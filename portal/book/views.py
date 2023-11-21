from django.shortcuts import render, redirect
import requests
import json

from .forms import SearchBookForm


def home(request):
    """
    display a search form to search books
    display 10 books searched
    api - https://www.googleapis.com/books/v1/volumes?q={search terms}
    """
    if request.method == "POST":
        form = SearchBookForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data.get("text")

            url = f"https://www.googleapis.com/books/v1/volumes?q={text}"
            response = requests.get(url)
            data = response.json()

            books = []
            for item in data["items"]:
                book = {}
                volume_info = item['volumeInfo']
                book['title'] = volume_info.get('title')
                book['subtitle'] = volume_info.get('subtitle')
                book['description'] = volume_info.get('description')
                book['count'] = volume_info.get('pageCount')
                book['categories'] = volume_info.get('categories')
                book['rating'] = volume_info.get('averageRating')
                book['thumbnail'] = volume_info.get('imageLinks', {}).get('thumbnail')
                book['preview'] = volume_info.get('previewLink')

                books.append(book)

            return render(request, "book/home.html", {
                "title": "books",
                "books": books,
                "form": form
            })

    else:
        form = SearchBookForm()

    return render(request, "book/home.html", {
        "title": "books",
        "form": form
    })

