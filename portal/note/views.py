from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Note


def home(request):
    """
    display the user notes
    add a form to create a new note
    """
    notes = Note.objects.filter(user=request.user)

    return render(request, "note/home.html", {
        "notes": notes,
        "title": "notes"
    })
