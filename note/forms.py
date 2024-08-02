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
            "title": "",
            "description": ""
        }

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-group my-3",
                "placeholder": "title"
                }),
            "description": forms.Textarea(attrs={
                "class": "form-group my-3",
                "placeholder": "Your notes..."
            })
        }