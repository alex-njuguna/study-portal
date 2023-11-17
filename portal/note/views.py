from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Note
from .forms import AddNoteForm


def home(request):
    """
    display the user notes
    add a form to create a new note
    """
    notes = Note.objects.filter(user=request.user)

    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            user = request.user
            title = title=form.cleaned_data.get("title")
            description=form.cleaned_data.get("description")

            note = Note(user=user, title=title, description=description)
            note.save()
            messages.success(request, f"Note: {title} saved")

            return redirect("note:home")
    else:
        form = AddNoteForm() 

    return render(request, "note/home.html", {
        "notes": notes,
        "title": "notes",
        "form": form
    })


def note_detail(request, id):
    """
    get a note by id
    display note details
    """
    note = Note.objects.get(user=request.user, id=id)

    return render(request, "note/note_detail.html", {
        "title": "detail",
        "note": note
    })


def note_delete(request, id):
    """
    get note by id
    capture note tite
    delete note
    """
    note = Note.objects.get(user=request.user, id=id)

    title = note.title
    note.delete()
    messages.info(request, f"Note: {title} deleted!")


    return redirect("note:home")
