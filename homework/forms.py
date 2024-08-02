from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import Homework


"""
fields borrowed from the Homwork model
styling with bootstrap
"""
class AddHomeworkForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Homework
        fields = ["subject", "title", "description", "due_date", "is_finished"]

        labels={
            "is_finished": "Mark complete",
            "subject": "",
            "title": ""
        }

        widgets = {
            "subject": forms.TextInput(attrs={
                "class": "form-control my-3",
                "placeholder": "subject"
            }),
            "title": forms.TextInput(attrs={
                "class": "form-control my-3",
                "placeholder": "title"
            }),
            "due_date": forms.DateTimeInput(attrs={
                "class": "form-control my-3",
                "type": "datetime-local"
            }),
            "is_finished": forms.CheckboxInput(attrs={
                "class": "mt-1"
            }),
        }
