import requests

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import FileResponse
from django.contrib.auth.decorators import login_required

from .forms import SearchBookForm, AddBookForm
from .models import Book


@login_required
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
                volume_info = item['volumeInfo']
                book = {
                    'title': volume_info.get('title'),
                    'subtitle': volume_info.get('subtitle'),
                    'description': volume_info.get('description'),
                    'count': volume_info.get('pageCount'),
                    'categories': volume_info.get('categories'),
                    'rating': volume_info.get('averageRating'),
                    'thumbnail': volume_info.get('imageLinks', {}).get('thumbnail'),
                    'preview': volume_info.get('previewLink')
                }

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


@login_required
def books(request):
    """
    add a book to the portal
    display all books
    """

    if request.method == "POST":
        form = AddBookForm(request.POST, request.FILES)

        if form.is_valid():
            user = request.user
            title = form.cleaned_data.get("title")
            contents = form.cleaned_data.get("contents")

            book = Book(user=user, title=title, contents=contents)

            book.save()
            messages.success(request, "New book added")

            return redirect("book:books")
    else:
       form = AddBookForm()

    books_list = Book.objects.filter(user=request.user)
    
    return render(request, "book/books.html", {
        "title": "books",
        "form": form,
        "books": books_list
    })

@login_required
def open_book(request, id):
    """open a book in browser"""
    book = Book.objects.get(user=request.user, id=id)

    if book.contents.name.endswith(".pdf"):
        content_type = "application/pdf"
    elif book.contents.name.endswith(".epub"):
        content_type = "application/epub+zip"
    else:
        raise ValueError("Unsupported file type")

    reading_file = open(book.contents.path, "rb")

    return FileResponse(reading_file, content_type=content_type)

@login_required
def delete_book(request, id):
    """delete a given book by id"""
    book = Book.objects.get(user=request.user, id=id)
    title = book.title
    book.delete()

    messages.info(request, f"'{title.capitalize()}' deleted.")

    return redirect("book:books")


