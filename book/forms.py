from django import forms

from .models import Book


"""
create a search youtube form 
fields - texarea
"""
class SearchBookForm(forms.Form):
    text = forms.CharField(max_length=100, label="", 
                                  widget=forms.TextInput(attrs={
                                      "class": "w-100"
                                  }))


"""form to upload a book"""
class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "contents"]

        labels = {
            "title": "Book Title: ",
            "contents": "(epub or pdf)"
        }

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control mb-3"
                }),
        }