from django import forms

from .models import Homework


"""
fields borrowed from the Homwork model
styling with bootstrap
"""
class AddHomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ["subject", "title", "description", "due", "is_finished"]
        widgets = {
            "subject": forms.TextInput(attrs={
                "class": "form-control mb-2",
                "placeholder": "e.g Web technologies"
            }),
            "title": forms.TextInput(attrs={
                "class": "form-control mb-2",
                "placeholder": "e.g http and https"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control mb-2",
                "placeholder": "e.g Explain the importance of https"
            }),
            "due": forms.DateTimeInput(attrs={
                "class": "form-control mb-2",
                "type": "datetime-local"
            }),
            "is_finished": forms.CheckboxInput(attrs={
                "class": "form-control"
            }),
        }
