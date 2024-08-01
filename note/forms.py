from django import forms

from .models import Note


class AddNoteForm(forms.ModelForm):
    """
    fields to add to form - title, description
    """
    class Meta:
        model = Note
        fields = ["title", "description"]

        labels = {
            "title": "Title: ",
            "description": "Things to note: "
        }

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-group mb-2",
                "placeholder": "e.g. Intro to redis"
                }),
            "description": forms.Textarea(attrs={
                "class": "form-group",
                "placeholder": "Your notes..."
            })
        }